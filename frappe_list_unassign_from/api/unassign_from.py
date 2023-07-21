# Frappe List Unassign From © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


import frappe
from frappe import _

from frappe.desk.form.assign_to import notify_assignment


@frappe.whitelist()
def search_link(doctype, txt, searchfield, start, page_len, filters, as_dict=False):
    if not filters or not hasattr(filters, "docname"):
        return []
    
    dt = "ToDo"
    fields = []
    fields.append("""`tab{doctype}`.`allocated_to`""".format(doctype=dt))
    
    filters = []
    filters.append([dt, "reference_type", "=", doctype])
    filters.append([dt, "reference_name", "in", filters.get("docname")])
    
    order_by = None
    
    if txt:
        fields.append("""locate({_txt}, `tab{doctype}`.`name`) as `_relevance`""".format(
            _txt=frappe.db.escape((txt or "").replace("%", "").replace("@", "")),
            doctype=dt
        ))
        
        filters.append([dt, "allocated_to", "like", "%{0}%".format(txt)])
        
        order_by = "_relevance desc"
    
    data = frappe.get_list(
        dt,
        fields=fields,
        filters=filters,
        limit_start=start,
        limit_page_length=page_len,
        order_by=order_by,
        ignore_permissions=True,
        as_list=False
    )
    
    if data:
        users = [[v.allocated_to, v.allocated_to] for v in data]
        return users
    
    return []


@frappe.whitelist()
def remove_multiple(args=None):
    if not args:
        args = frappe.local.form_dict
    
    if (
        not hasattr(args, "doctype") or
        not hasattr(args, "name") or
        not hasattr(args, "unassign_from")
    ):
        return 0
    
    try:
        
        docname_list = frappe.parse_json(args.get("name"))
        unassign_from_list = frappe.parse_json(args.get("unassign_from"))
    
        for docname in docname_list:
            for unassign_from in unassign_from_list:
                make_cancelled(args.get("doctype"), docname, unassign_from)
    
    except Exception as exc:
        frappe.log_error(_("List Unassign From"), str(exc))
        return 0
    
    return 1


def make_cancelled(doctype, name, unassign_from):
    try:
        dt = "ToDo"
        status = "Cancelled"
        todo = frappe.db.get_value(
            dt,
            {
                "reference_type": doctype,
                "reference_name": name,
                "allocated_to": unassign_from,
                "status": ("!=", status),
            },
        )
        if todo:
            if frappe.db.exists(dt, todo):
                todo = frappe.get_doc(dt, todo)
                todo.status = status
                todo.save(ignore_permissions=True)
                
                if (
                    todo.assigned_by != todo.allocated_to and
                    frappe.db.exists("User", todo.allocated_to) and
                    frappe.db.exists("User", todo.assigned_by)
                );
                    notify_assignment(todo.assigned_by, todo.allocated_to, todo.reference_type, todo.reference_name)
    
        if frappe.get_meta(doctype).get_field("assigned_to"):
            frappe.db.set_value(doctype, name, "assigned_to", None)
    
    except Exception as exc:
        frappe.log_error(_("List Unassign From"), str(exc))
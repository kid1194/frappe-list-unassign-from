# Frappe List Unassign From © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


import frappe
from frappe import _
from frappe import __version__ as frappe_version

from frappe.desk.form.assign_to import notify_assignment


@frappe.whitelist(methods=["POST"])
def search_link(doctype, txt, filters):
    if not filters or not hasattr(filters, "docnames"):
        return []
    
    dt = "ToDo"
    is_frappe_above_v13 = int(frappe_version.split('.')[0]) > 13
    allocated_to = "allocated_to" if is_frappe_above_v13 else "owner"
    
    fields = []
    fields.append("""`tab{doctype}`.`{column}`""".format(
        doctype=dt,
        column=allocated_to
    ))
    fields.append("""`tab{doctype}`.`{column}`""".format(
        doctype=dt,
        column=allocated_to
    ))
    
    filters = []
    filters.append([dt, "status", "=", "Open"])
    filters.append([dt, "reference_type", "=", doctype])
    filters.append([dt, "reference_name", "in", filters.get("docnames")])
    
    order_by = None
    
    if txt:
        fields.append("""locate({_txt}, `tab{doctype}`.`{column}`) as `_relevance`""".format(
            _txt=frappe.db.escape((txt or "").replace("%", "").replace("@", "")),
            doctype=dt,
            column=allocated_to
        ))
        
        filters.append([dt, allocated_to, "like", "%{0}%".format(txt)])
        
        order_by = "_relevance desc"
    
    values = frappe.get_list(
        dt,
        fields=fields,
        filters=filters,
        limit_start=0,
        limit_page_length=20,
        order_by=order_by,
        ignore_permissions=True,
        as_list=True,
        strict=False
    )
    
    if values and txt:
        values = [r[:-1] for r in values]
    
    return values


@frappe.whitelist()
def remove_multiple(args=None):
    if not args:
        args = frappe.local.form_dict
    
    if (
        not hasattr(args, "doctype") or
        not hasattr(args, "docnames") or
        not hasattr(args, "unassign_from")
    ):
        return 0
    
    try:
        
        docnames_list = frappe.parse_json(args.get("docnames"))
        unassign_from_list = frappe.parse_json(args.get("unassign_from"))
    
        for docname in docnames_list:
            for unassign_from in unassign_from_list:
                make_cancelled(args.get("doctype"), docname, unassign_from)
    
    except Exception as exc:
        frappe.log_error(_("List Unassign From"), str(exc))
        return 0
    
    return 1


def make_cancelled(doctype, docname, unassign_from):
    try:
        dt = "ToDo"
        is_frappe_above_v13 = int(frappe_version.split('.')[0]) > 13
        allocated_to = "allocated_to" if is_frappe_above_v13 else "owner"
        status = "Cancelled"
        
        args = {
            "reference_type": doctype,
            "reference_name": docname,
            "status": ("!=", status),
        }
        args[allocated_to] = unassign_from
        
        todo = frappe.db.get_value(dt, args)
        if todo:
            if frappe.db.exists(dt, todo):
                todo = frappe.get_doc(dt, todo)
                todo.status = status
                todo.save(ignore_permissions=True)
                
                if (
                    todo.assigned_by != todo.get(allocated_to) and
                    frappe.db.exists("User", todo.get(allocated_to)) and
                    frappe.db.exists("User", todo.assigned_by)
                ):
                    notify_assignment(
                        todo.assigned_by,
                        todo.get(allocated_to),
                        todo.reference_type,
                        todo.reference_name
                    )
        
        if frappe.get_meta(doctype).get_field("assigned_to"):
            frappe.db.set_value(doctype, docname, "assigned_to", None)
    
    except Exception as exc:
        frappe.log_error(_("List Unassign From"), str(exc))
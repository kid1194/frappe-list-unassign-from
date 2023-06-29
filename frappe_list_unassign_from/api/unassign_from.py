# Frappe List Unassign Form © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


import frappe
from frappe.desk.form.assign_to import set_status


@frappe.whitelist()
def search_link(doctype, txt, searchfield, start, page_len, filters):
    if not hasattr(filters, "docname"):
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

    docname_list = frappe.parse_json(args.get("name"))
    unassign_from_list = frappe.parse_json(args.get("unassign_from"))

    for docname in docname_list:
        for unassign_from in unassign_from_list:
            set_status(args.get("doctype"), docname, unassign_from, status="Cancelled")
    
    return 1
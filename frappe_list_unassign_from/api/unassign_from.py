# Frappe List Unassign From © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


import frappe
from frappe import _

from frappe.desk.form.assign_to import notify_assignment

from frappe_list_unassign_from.version import __frappe_version_min_14__


@frappe.whitelist()
def remove_multiple(args=None):
    if not args:
        args = frappe.local.form_dict
    
    if (
        not args or
        not isinstance(args, dict) or
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
        allocated_to = "allocated_to" if __frappe_version_min_14__ else "owner"
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
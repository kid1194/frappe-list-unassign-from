import frappe
from frappe.query_builder.functions import Locate
from pypika.enums import Order
from frappe.desk.form.assign_to import set_status

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def search_link(doctype, txt, searchfield, start, page_len, filters):
    if not hasattr(filters, 'docname'):
        return []
    
    dToDo = frappe.qb.DocType('ToDo')
    qTodo = (
        frappe.qb.from_(dToDo)
        .where(dToDo.reference_type == doctype)
        .where(dToDo.reference_name.isin(filters.get('docname')))
        .limit(page_len)
        .offset(start)
    )
    
    if not txt:
        qTodo.select(dToDo.allocated_to)
    else:
        qTodo.select(dToDo.allocated_to, Locate(txt, dToDo.allocated_to).as_('_relevance'))
        qTodo.where(dToDo.allocated_to.like(f'%{txt}%'))
        qTodo.orderby('_relevance', order=Order.desc)
    
    data = qTodo.run(as_dict=True)
    users = [[v.allocated_to, v.allocated_to] for v in data]
    return users

@frappe.whitelist()
def remove_multiple(args=None):
	if not args:
		args = frappe.local.form_dict

	docname_list = frappe.parse_json(args.get("name"))
	unassign_from_list = frappe.parse_json(args.get("unassign_from"))

	for docname in docname_list:
	    for unassign_from in unassign_from_list:
		    set_status(args.get("doctype"), docname, unassign_from, status="Cancelled")

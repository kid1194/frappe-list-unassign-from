# Frappe List Unassign Form © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from frappe import _


def get_data():
    return [
        {
            "module_name": "Frappe List Unassign From",
            "color": "blue",
            "icon": "octicon octicon-table",
            "type": "module",
            "label": _("Frappe List Unassign From")
        }
    ]
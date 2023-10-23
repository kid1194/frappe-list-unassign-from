# Frappe List Unassign From © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from .version import __frappe_version_min_14__


app_name = "frappe_list_unassign_from"
app_title = "Frappe List Unassign From"
app_publisher = "Ameen Ahmed (Level Up)"
app_description = "A Frappe plugin that adds the support of unassign from users for single and multiple list selection."
app_icon = "octicon octicon-table"
app_color = "blue"
app_email = "kid1194@gmail.com"
app_license = "MIT"


app_include_js = [
    "unassign_from.bundle.js"
] if __frappe_version_min_14__ else [
    "/assets/frappe_list_unassign_from/js/unassign_from.js"
]
# Frappe List Unassign Form © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from . import __version__ as app_version
from frappe import __version__ as frappe_version


app_name = "frappe_list_unassign_from"
app_title = "Frappe List Unassign From"
app_publisher = "Ameen Ahmed (Level Up)"
app_description = "A Frappe plugin that adds the support of project tasks single or multiple unassign."
app_icon = "octicon octicon-table"
app_color = "blue"
app_email = "kid1194@gmail.com"
app_license = "MIT"
is_frappe_above_v13 = int(frappe_version.split(".")[0]) > 13


app_include_js = [
    "unassign_from.bundle.js"
] if is_frappe_above_v13 else [
    "/assets/frappe_list_unassign_from/js/unassign_from.js"
]
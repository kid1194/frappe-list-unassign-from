# Frappe List Unassign From
A Frappe plugin that adds the support of unassign from for multiple selection in list.

### Table of Contents
<ul>
    <li><a href="#requirements">Requirements</a></li>
    <li>
        <a href="#setup">Setup</a>
        <ul>
            <li><a href="#install">Install</a></li>
            <li><a href="#update">Update</a></li>
            <li><a href="#uninstall">Uninstall</a></li>
        </ul>
    </li>
    <li><a href="#license">License</a></li>
</ul>

---

### Requirements
- Frappe >= v13.0.0

---

### Setup

#### Install
1. Get the plugin from Github

*(Required only once)*

`bench get-app https://github.com/kid1194/frappe-list-unassign-from`

2. Install the plugin on any instance/site you want

`bench --site [sitename] install-app frappe_list_unassign_from`

3. Check the usage section below

#### Update
1. Go to the app directory (frappe-bench/apps/frappe_list_unassign_from) and execute:

`git pull`

2. Go back to the frappe-bench directory and execute:

`bench --site [sitename] migrate`

3. *In case you need to restart bench, execute:*

`bench restart`

#### Uninstall
1. Uninstall the plugin from the instance/site

`bench --site [sitename] uninstall-app frappe_list_unassign_from`

2. Uninstall the plugin from bench

`bench remove-app frappe_list_unassign_from`

---

### License
MIT

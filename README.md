# Frappe List Unassign From

A Frappe plugin that adds the support of unassign from users for single and multiple list selection.

---

### Special Thanks 
**A simple display of gratitude and appreciation to those who provided help and kind support.**
- [RJPvT](https://github.com/RJPvT) (Testing)
- [Ragul KM](https://github.com/crazy-explore-r) (Bug Reporting & Screenshots)

---

<div style="width:100%;text-align:center">
    <img src="https://github.com/kid1194/frappe-list-unassign-from/blob/main/images/list_unassign_from_1.jpg?raw=true" alt="List Unassign From"/>
</div>
<div style="width:100%;text-align:center">
    <img src="https://github.com/kid1194/frappe-list-unassign-from/blob/main/images/list_unassign_from_2.jpg?raw=true" alt="List Unassign From"/>
</div>

---

### Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install](#install)
  - [Update](#update)
  - [Uninstall](#uninstall)
- [Usage](#usage)
- [Issues](#issues)
- [License](#license)

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

### Usage
1. Go to any doctype's list, ex: **Role**, and select a single or multiple entries
2. Click on the **Actions** button from the top of the page and click on **Unassign From** action
3. From the **Remove From ToDo** dialog, add the users that you want to unassign the entries from
4. Finally, click on the **Remove** button at the bottom of the dialog

---

### Issues
If you find bug in the plugin, please create a [bug report](https://github.com/kid1194/frappe-list-unassign-from/issues/new?assignees=kid1194&labels=bug&template=bug_report.md&title=%5BBUG%5D) and let us know about it.

---

### License
This repository has been released under the [MIT License](https://github.com/kid1194/frappe-list-unassign-from/blob/main/LICENSE).

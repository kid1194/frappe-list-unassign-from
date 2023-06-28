# Frappe List Unassign From

A Frappe plugin that adds the support of unassign from for multiple selection in list.

---

### Special Thanks 
**A simple display of gratitude and appreciation to those who provided helped and kind support.**
- [RJPvT](https://github.com/RJPvT) (Testing)

---

### Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install](#install)
  - [Update](#update)
  - [Uninstall](#uninstall)
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

### Issues
If you find bug in the plugin, please create a [bug report](https://github.com/kid1194/frappe-list-unassign-from/issues/new?assignees=kid1194&labels=bug&template=bug_report.md&title=%5BBUG%5D) and let us know about it.

---

### License
This repository has been released under the [MIT License](https://github.com/kid1194/frappe-list-unassign-from/blob/main/LICENSE).

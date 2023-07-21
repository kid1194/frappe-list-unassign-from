/*
* Frappe List Unassign From © 2023
* Author:  Ameen Ahmed
* Company: Level Up Marketing & Software Development Services
* Licence: Please refer to LICENSE file
*/


import {
    UnassignFromDialog
} from './unassign_from_dialog.js';

export class CustomBulkOperations {
    constructor({ doctype }) {
        if (!doctype) frappe.throw(__('Doctype is not provided'));
        this.doctype = doctype;
    }
    // unassignment
    unassign(docnames, done) {
        if (docnames.length > 0) {
            var unassign_from = new UnassignFromDialog({
                obj: this,
                method: 'frappe_list_unassign_from.api.remove_multiple',
                doctype: this.doctype,
                docname: docnames,
                callback: done
            });
            unassign_from.dialog.clear();
            unassign_from.dialog.show();
        } else {
            frappe.msgprint(__('Select a single or multiple entries to unassign users from'));
        }
    }
}
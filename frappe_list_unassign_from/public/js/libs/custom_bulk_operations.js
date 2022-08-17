import {UnassignFromDialog} from './unassign_from_dialog.js';

export default class CustomBulkOperations {
    constructor({ doctype }) {
        if (!doctype) frappe.throw(__('Doctype required'));
        this.doctype = doctype;
    }
    // unassignment
    unassign(docnames, done) {
        if (docnames.length > 0) {
            const unassign_from = new UnassignFromDialog({
                obj: this,
                method: 'frappe_list_unassign_from.api.unassign_from.remove_multiple',
                doctype: this.doctype,
                docname: docnames,
                callback: done
            });
            unassign_from.dialog.clear();
            unassign_from.dialog.show();
        } else {
            frappe.msgprint(__('Select records to remove assignment'));
        }
    }
}

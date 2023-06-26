/*
* Frappe List Unassign Form © 2023
* Author:  Ameen Ahmed
* Company: Level Up Marketing & Software Development Services
* Licence: Please refer to LICENSE file
*/


export class UnassignFromDialog {
    constructor(opts) {
        $.extend(this, opts);

        this.make();
        this.set_description_from_doc();
    }
    make() {
        var me = this;

        me.dialog = new frappe.ui.Dialog({
            title: __('Remove from ToDo'),
            fields: me.get_fields(),
            primary_action_label: __('Remove'),
            primary_action: function() {
                var args = me.dialog.get_values();

                if (args && args.unassign_from) {
                    me.dialog.set_message('Unassigning...');

                    frappe.call({
                        method: me.method,
                        args: $.extend(args, {
                            doctype: me.doctype,
                            name: me.docname,
                            unassign_from: args.unassign_from
                        }),
                        btn: me.dialog.get_primary_btn(),
                        callback: function(r) {
                            if (!r.exc) {
                                if (me.callback) {
                                    me.callback(r);
                                }
                                me.dialog && me.dialog.hide();
                            } else {
                                me.dialog.clear_message();
                            }
                        },
                    });
                }
            },
        });
    }
    unassign_from_me() {
        var me = this,
        unassign_from = [];

        if (me.dialog.get_value('unassign_from_me')) {
            unassign_from.push(frappe.session.user);
        }

        me.dialog.set_value('unassign_from', unassign_from);
    }
    set_description_from_doc() {
        var me = this;

        if (me.frm && me.frm.meta.title_field) {
            me.dialog.set_value('description', me.frm.doc[me.frm.meta.title_field]);
        }
    }
    get_fields() {
        var me = this;

        return [
            {
                label: __('Unassign from me'),
                fieldtype: 'Check',
                fieldname: 'unassign_from_me',
                default: 0,
                onchange: function() { me.unassign_from_me() }
            },
            {
                fieldtype: 'MultiSelectPills',
                fieldname: 'unassign_from',
                label: __('Unassign From'),
                reqd: true,
                get_data: function(txt) {
                    var args = {
                        doctype: me.doctype,
                        txt: txt,
                        query: 'frappe_list_unassign_from.api.search_link',
                        filters: {docname: me.docname}
                    };
                    return new Promise(function(resolve, reject) {
                        frappe.call({
                            type: 'GET',
                            method: 'frappe.desk.search.search_link',
                            args: args,
                            callback: function(r) {
                                resolve(r.values);
                            }
                        });
                    });
                }
            }
        ];
    }
}
/*
* Frappe List Unassign From © 2023
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
        this.dialog = new frappe.ui.Dialog({
            title: __('Remove From ToDo'),
            fields: this.get_fields(),
            primary_action_label: __('Remove'),
            primary_action: function() {
                var args = me.dialog.get_values();
                if (args) {
                    var unassign_from = args.unassign_from;
                    if (!$.isArray(unassign_from)) unassign_from = [];
                    if (args.unassign_from_me) unassign_from.unshift(frappe.session.user);
                    me.dialog.set_message(__('Unassigning') + '...');
                    frappe.call({
                        method: me.method,
                        args: $.extend(args, {
                            doctype: me.doctype,
                            docnames: me.docnames,
                            unassign_from: unassign_from
                        }),
                        btn: me.dialog.get_primary_btn(),
                        callback: function(r) {
                            if (!r.exc) {
                                if (me.callback) me.callback(r);
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
    set_description_from_doc() {
        if (this.frm && this.frm.meta.title_field)
            this.dialog.set_value('description', this.frm.doc[this.frm.meta.title_field]);
    }
    get_fields() {
        var me = this;
        return [
            {
                label: __('Unassign from me'),
                fieldtype: 'Check',
                fieldname: 'unassign_from_me',
                default: 0,
            },
            {
                fieldtype: 'MultiSelectPills',
                fieldname: 'unassign_from',
                label: __('Unassign From'),
                reqd: true,
                onchange: function() {
                    try {
                        var vals = this.get_values(),
                        idx = vals.indexOf(frappe.session.user);
                        if (idx >= 0) {
                            vals.splice(idx, 1);
                            me.dialog.set_value('unassign_from_me', 1);
                            me.dialog.set_value('unassign_from', vals);
                        }
                    } catch(_) {}
                },
                get_data: function(txt) {
                    return frappe.db.get_link_options('User', txt, {user_type: 'System User', enabled: 1});
                }
            }
        ];
    }
}
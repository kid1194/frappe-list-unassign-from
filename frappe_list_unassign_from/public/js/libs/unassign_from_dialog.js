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
                if (args && args.unassign_from) {
                    me.dialog.set_message(__('Unassigning') + '...');
                    frappe.call({
                        method: me.method,
                        args: $.extend(args, {
                            doctype: me.doctype,
                            docnames: me.docnames,
                            unassign_from: args.unassign_from
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
    unassign_from_me() {
        if (this.dialog.get_value('unassign_from_me')) {
            var unassign_from = this.dialog.get_value('unassign_from');
            if (!$.isArray(unassign_from))
                unassign_from = [frappe.session.user];
            else unassign_from.unshift(frappe.session.user);
            this.dialog.set_value('unassign_from', unassign_from);
        }
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
                        filters: {docnames: me.docnames}
                    };
                    new Promise(function(resolve, reject) {
                        frappe.call({
                            type: 'POST',
                            method: 'frappe_list_unassign_from.api.search_link',
                            args: args,
                            callback: function(ret) {
                                console.log('[UnassignFromDialog]', ret);
                                if (ret && $.isPlainObject(ret)) ret = ret.message || ret;
                                resolve(ret);
                            },
                            error: function() {
                                console.error('[UnassignFromDialog]', 'request error');
                                reject();
                            }
                        });
                    });
                    return frappe.db.get_link_options('User', txt, {user_type: 'System User', enabled: 1});
                }
            }
        ];
    }
}
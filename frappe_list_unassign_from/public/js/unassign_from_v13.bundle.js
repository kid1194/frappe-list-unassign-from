/*
* Frappe List Unassign Form © 2023
* Author:  Ameen Ahmed
* Company: Level Up Marketing & Software Development Services
* Licence: Please refer to LICENSE file
*/


import {
    CustomBulkOperations
} from './libs/custom_bulk_operations.js';


frappe.views.ListView = class ListView extends frappe.views.ListView {
    get_actions_menu_items() {
        var me = this,
        doctype = this.doctype,
        actions_menu_items = super.get_actions_menu_items(),
        bulk_operations = new CustomBulkOperations({doctype: this.doctype}),

        is_field_editable = function(field_doc) {
            return (
                field_doc.fieldname &&
                frappe.model.is_value_type(field_doc) &&
                field_doc.fieldtype !== 'Read Only' &&
                !field_doc.hidden &&
                !field_doc.read_only &&
                !field_doc.is_virtual
            );
        },

        has_editable_fields = function(doctype) {
            return frappe.meta
                .get_docfields(doctype)
                .some(function(field_doc) { return is_field_editable(field_doc); });
        },
        
        // unassignment
        bulk_unassignment = function() {
            return {
                label: __('Unassign From', null, 'Button in list view actions menu'),
                action: function() {
                    bulk_operations.unassign(
                        me.get_checked_items(true),
                        function() {
                            me.refresh();
                        }
                    );
                },
                standard: true,
            };
        },
        
        idx = 2;
        // bulk edit
        if (has_editable_fields(doctype)) idx++;
        // unassignment
        actions_menu_items.splice(idx, 0, bulk_unassignment());
        
        return actions_menu_items;
    }
};
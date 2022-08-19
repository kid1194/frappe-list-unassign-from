import {
    CustomBulkOperations
} from './libs/custom_bulk_operations.js';

frappe.views.ListView = frappe.views.ListView.extend({
    get_actions_menu_items: function() {
        const doctype = this.doctype;
        const actions_menu_items = this._super();
        const bulk_operations = new CustomBulkOperations({doctype: this.doctype});

        const is_field_editable = (field_doc) => {
            return (
                field_doc.fieldname &&
                frappe.model.is_value_type(field_doc) &&
                field_doc.fieldtype !== "Read Only" &&
                !field_doc.hidden &&
                !field_doc.read_only &&
                !field_doc.is_virtual
            );
        };

        const has_editable_fields = (doctype) => {
            return frappe.meta
                .get_docfields(doctype)
                .some((field_doc) => is_field_editable(field_doc));
        };
        
        // unassignment
        const bulk_unassignment = () => {
            return {
                label: __("Unassign From", null, "Button in list view actions menu"),
                action: () => {
                    bulk_operations.unassign(
                        this.get_checked_items(true),
                        () => {
                            this.refresh();
                        }
                    );
                },
                standard: true,
            };
        };
        
        let idx = 2;
        // bulk edit
        if (has_editable_fields(doctype)) idx++;
        // unassignment
        actions_menu_items.splice(idx, 0, bulk_unassignment());

        return actions_menu_items;
    }
});

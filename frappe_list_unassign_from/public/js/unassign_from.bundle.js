import {CustomBulkOperations} from './libs/custom_bulk_operations.js';

frappe.views.ListView = class ListView extends frappe.views.ListView {
    get_actions_menu_items() {
        const doctype = this.doctype;
        const actions_menu_items = super.get_actions_menu_items();
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
        
        const is_v13 = cint(String(window._version_number).split('.')[0]) < 14;
        
        // unassignment
        const bulk_unassignment = () => {
            return {
                label: __("Unassign From", null, "Button in list view actions menu"),
                action: () => {
                    if (!is_v13) this.disable_list_update = true;
                    bulk_operations.unassign(
                        this.get_checked_items(true),
                        () => {
                            if (!is_v13) {
                                this.disable_list_update = false;
                                this.clear_checked_items();
                            }
                            this.refresh();
                        }
                    );
                },
                standard: true,
            };
        };
        
        let idx = 2;
        if (!is_v13) idx++;
        // bulk edit
        if (has_editable_fields(doctype)) idx++;
        // unassignment
        actions_menu_items.splice(idx, 0, bulk_unassignment());

        return actions_menu_items;
    }
};

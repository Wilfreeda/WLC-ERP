// Copyright (c) 2024, WLC. and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Enrollment", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Enrollment", {
    refresh:function(frm){
        frm.fields_dict['validity_extension'].grid.wrapper.find('.grid-add-row').hide();
        if (frm.doc.enrollment_status != "Cancelled") {
            frm.add_custom_button(__("Extend Validity"), function() {
                let d = new frappe.ui.Dialog({
                    title: 'Extend Validity',
                    fields: [{
                            label: 'Entry Date',
                            fieldname: 'entry_date',
                            fieldtype: 'Date',
                            default: 'Today',
                            read_only: 1
                        },
                        {
                            label: 'Extend the validity for',
                            fieldname: 'days',
                            fieldtype: 'Duration',
                            "hide_seconds": 1,
                            reqd: 1
                        },
                        {
                            label: 'Reason for extension',
                            fieldname: 'notes',
                            fieldtype: 'Small Text',
                            reqd: 1
                        }
                    ],
                    primary_action_label: ('Submit'),
                    primary_action: function() {
                        d.hide();
                        frm.save();
                        let row = frappe.model.add_child(frm.doc, 'Validity Extension', 'validity_extension');
                        frappe.model.set_value(row.doctype, row.name, 'entry_date', d.get_value('entry_date'));
                        frappe.model.set_value(row.doctype, row.name, 'days', d.get_value('days'));
                        frappe.model.set_value(row.doctype, row.name, 'notes', d.get_value('notes'));
                    }
                });
                d.show()

            })

            frm.add_custom_button(__("All Topics Progress"), function() {
                frappe.route_options = { "enrollment_id": frm.doc.name }
                frappe.set_route('List', 'Topic Progress')
            }, __("View"))
        }
    }
})

frappe.ui.form.on("Enrollment Subject Item", {
    subject_progress_button: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        frappe.route_options = { "enrollment_id": frm.doc.name, 'topic_id': d.topic_id }
        frappe.set_route('Form', 'Topic Progress')
    }
})
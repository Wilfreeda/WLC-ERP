// Copyright (c) 2024, WLC. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student", {
	refresh: (frm) => {
        if (frm.doc.student_status != 'Disabled') {
            frm.add_custom_button(__('Disable'), () => {
                frappe.confirm('Disable this student' , () => {
                    frm.set_value('student_status', 'Disable')
                    frm.save()
                    .then(() => {
                        frappe.msgprint({
                            title: __('Nofication'),
                            indicator: 'red',
                            message: __('This student has been disabled')
                        })
                    })
                }, () => {
                    // action to perform if no is selected
                })
            })
        }
	},
});
// Copyright (c) 2024, WLC. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Class Schedule", {
	validate: function(frm) {
		var class_from = frm.doc.class_from;
        var class_to = frm.doc.class_to;

        if (class_from && class_to) {
            var from_time = new Date(class_from);
            var to_time = new Date(class_to);

            if (to_time < from_time) {
                frappe.msgprint(__("Class To Time must be greater than Class From Time."));
                frappe.validated = false;
                returnl
            }

            var duration = (to_time - from_time) / (1000 * 60 * 60);

            if (duration > 8 || duration < 0.25) {
                frappe.msgprint(__('The class duration is {0} hours based on the time you have selected. Class duration must be between 15 minutes and 8 hours.', [duration.toFixed(2)]))
                frappe.validated = false;
                return;
            }
        }
	}
});

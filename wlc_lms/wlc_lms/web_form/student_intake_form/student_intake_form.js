frappe.ready(function() {
	frappe.web_form.on('course_name', function() {
		var course_name = frappe.web_form.get_value('course_name');
		if (course_name) {
            frappe.call({
                method: 'wlc_lms.wlc_lms.doctype.wlc_student_intake.wlc_student_intake.get_course_levels', 
                args: {
                    course_name: course_name
                },
                callback: function(r) {
                    console.log(r.message);
                    frappe.web_form.set_df_property('course_level_or_type', 'options', r.message);
                }
            })
        }
	})
})
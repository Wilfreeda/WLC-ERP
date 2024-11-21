frappe.listview_settings['Enrollment'] = {
    add_fields: ["student_name", "course_name", "enrollment_status", "expiry_date", "overall_progress"],

    hide_name_column: true,
    get_idicator: function(doc) {
        if (doc.enrollment_status === 'Active') {
            return [__("Active"), "green", "enrollment_status,=,Active"];
        } else if (doc.enrollment_status === 'Expired') {
            return [__("Expired"), "red", "enrollment_status,=,Expired"];
        } else if (doc.enrollment_status === 'Inactive') {
            return [__("Inactive"), "gray", "enrollment_status,=,Inactive"]
        }
    }
}
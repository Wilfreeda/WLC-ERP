frappe.listview_settings['Class Schedule'] = {
    hide_name_colum: true,
    add_fields: ['class_status', 'class_from', 'educator', 'student'],
    get_indicator: function(doc) {
        if (doc.class_status === "Draft") {
            return[__('Draft'), "yellow", "class_status,=,Draft"];
        } else if  (doc.class_status === "Scheduled") {
            return[__('Scheduled'), "green", "class_status,=,Scheduled"];
        } else if (doc.class_status === "Open") {
            return[__('Open'), "purple", "class_status,=,Open"];
        } else if (doc.class_status === "Complete") {
            return[__('Complete'), "red", "class_status,=,Complete"];
        } else if (doc.class_status === "Cancelled") {
            return[__('Cancelled'), "red", "class_status,=,Cancelled"];
        }
    }
}
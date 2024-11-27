// Copyright (c) 2024, rino and contributors
// For license information, please see license.txt

frappe.ui.form.on("WLC Student Intake", {
	refresh: function(frm) {
        console.log('hll0')
        if (frm.doc.course_name) {
            frappe.call({
                method: 'wlc_lms.wlc_lms.doctype.wlc_student_intake.wlc_student_intake.get_course_levels', 
                args: {
                    course_name: frm.doc.course_name
                },
                callback: function(r) {
                    console.log(r.message);
                    frm.set_df_property('course_level_or_type', 'options', r.message);
                    frm.refresh_field('course_level_or_type');
                }
            })
        }
    },
    course_name: function(frm) {
        if (frm.doc.course_name) {
            frappe.call({
                method: 'wlc_lms.wlc_lms.doctype.wlc_student_intake.wlc_student_intake.get_course_levels',
                args: {
                    course_name: frm.doc.course_name,
                },
                callback: function(res) {
                    console.log(res.message);
                    frm.set_df_property('course_level_or_type', 'options', res.message);
                    frm.refresh_field('course_level_or_type');
                }
            })
        } else {
            frm.set_df_property('course_level_or_type', 'options', []);
            frm.refresh_field('course_level_or_type');
        }
    }
});


// frappe.ui.form.on("WLC Student Intake", function (frm) {
//     // frm.set_query("course_name", function() {
//     //     if (!frm.doc.course_name) {
//     //         frappe.msgprint({
//     //             title: __('Required info missing'),
//     //             message: __('Please select a course first'),
//     //             indicator: 'red'
//     //         });
//     //     } else {
//     //         console.log("happy")
//     //         return {
//     //             query: "wlc_lms.wlc_lms.doctype.wlc_student_intake.wlc_student_intake.get_course_levels_options",
//     //             filters: {
//     //                 course_name: frm.doc.course_name
//     //             }
//     //         }
//     //     }
//     // })

//     // console.log('dsfafvsd')

// });
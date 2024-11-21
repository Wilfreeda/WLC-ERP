

import frappe
from frappe.auth import get_logged_user

@frappe.whitelist()
def get_enrollments():
    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_logo = str(lms_settings.hostname) + str(lms_settings.default_image)

    token_user = get_logged_user()
    student = frappe.get_doc("Student", {"email": token_user})
    doc = frappe.get_doc('Student', student.name)

    enrollment_list = frappe.get_all('Student Enrollment', filters={'student_id': doc.name})
    
    my_courses = []
    if enrollment_list:
        for enrollments in enrollment_list:
            enrollment = frappe.get_doc('Student Enrollment', enrollments.name)
            course = frappe.get_doc('Course', enrollment.course_name)

            if course.course_image:
                course_image = str(lms_settings.hostname) + str(course.course_image)
            else:
                course_image = default_logo

            educator = frappe.get_doc('Educator', enrollment.educator)
            
            my_courses.append({
                'course_name': course.name,
                'enrollment_id': enrollment.name,
                'course_image': course_image,
                'educator': educator.full_name,
                'rating': course.rating,
                'course_description': course.course_description,
                # 'course_duration': course.course_duration,
                'course_start_date': enrollment.activation_date,
                # 'course_end_date': enrollment.end_date,
                'course_status': enrollment.enrollment_status
            })

        frappe.response["message"] = {
            "status": 1,
            "message": "Enrollments fetched successfully",
            "my_courses": my_courses
        }
    else:
        frappe.response["message"] = {
            "status": 0,
            "message": "No enrollments found"
        }


@frappe.whitelist()
def get_enrollment(enrollment_id):
    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_logo = str(lms_settings.hostname) + str(lms_settings.default_image)

    token_user = get_logged_user()
    student = frappe.get_doc("Student", {"email": token_user})
    doc = frappe.get_doc('Student', student.name)

    enrollment = frappe.get_doc('Student Enrollment', enrollment_id)

    class_schedules = frappe.get_all('Class Schedule', filters={'enrollment_id': enrollment.name, 'class_status': "Scheduled"})

    frappe.response['messages'] = {
        'status': 1,
        'message': 'Class schedules fetched successfully',
        'class_schedules': class_schedules,
        # 'enrollment': enrollment,
        # 'course_image': default_logo
    }

    
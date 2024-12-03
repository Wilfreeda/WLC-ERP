
import frappe

@frappe.whitelist(allow_guest = True)
def guest_init():
    course_list = []

    lms_settings = frappe.get_doc("WLC LMS Settings")
    support_number = lms_settings.support_number
    support_email = lms_settings.support_email_address
    wa_number = lms_settings.whatsapp_number

    courses = frappe.get_all('Course', fields=['*'], filters={'enabled': 1})

    for course in courses:
        course_list.append(course.name)

    frappe.response['messages'] = {
        'status': 1,
        'message': 'Course list fetched successfully',
        'course_list': course_list,
        'whatsapp_number': wa_number,
        'support_number': support_number,
        'support_email': support_email
    }

import frappe

@frappe.whitelist(allow_guest = True)
def guest_init():
    course_list = []

    courses = frappe.get_all('Course', fields=['*'], filters={'enabled': 1})

    for course in courses:
        course_list.append(course.name)

    frappe.response['messages'] = {
        'status': 1,
        'message': 'Course list fetched successfully',
        'course_list': course_list
    }
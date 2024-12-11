
import frappe

@frappe.whitelist(allow_guest=True)
def get_course_details(course_id):
    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_logo = str(lms_settings.hostname) + str(lms_settings.default_image)

    course = frappe.get_doc('Course', course_id)
    if course.course_image:
        course_image = str(lms_settings.hostname) + str(course.course_image)
    else:
        course_image = default_logo

    course_name = course.name
    description = course.course_description

    long_description = ''
    if course.long_description:
        long_description = course.long_description

    skills = []
    if course.skills:
        for skill in course.skills:
            skills.append(skill.skill)
                          
    why_this_couse = []
    if course.why:
        for why in course.why:
            why_this_couse.append({why.title: why.description})
    
    reasons = []
    if course.reasons:
        for reason in course.reasons:
            reasons.append({reason.title: reason.description})

    course_items = {}
    if course.topic_table:
        for item in course.topic_table:
            course_items[item.topic_name] = item.weightage

    frappe.response['message'] = {
        'status': 1,
        'message': 'Course details fetched successfully',
        'course_name': course_name,
        'skills': skills,
        'short_description': description,
        'long_description': long_description,
        'why_this_course': why_this_couse,
        'reasons': reasons,
        'course_items': course_items,
        'course_image': course_image
    }


@frappe.whitelist(allow_guest=True)
def get_course_list():
    course_list = []

    lms_settings = frappe.get_doc("WLC LMS Settings")
    
    courses = frappe.get_all("Course", filters={'show_on_web': 1, 'enabled': 1})

    if courses:
        for course in courses:
            course_doc = frappe.get_doc('Course', course.name)

            course_list.append({
                "course_id": course_doc.name,
                "course_name": course_doc.name,
                "course_image": course_doc.course_image,
                "description": course_doc.course_description,
            })
        
        frappe.response['messages'] = {
            'status': 1,
            'courses': course_list
        }
    
    else:
        frappe.response['messages'] = {
            'status': 0,
            'error': 'No courses found'
        }
    return
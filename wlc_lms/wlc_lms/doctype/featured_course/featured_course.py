# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt
# Developed by Rino Ruth Ricardo

import frappe
from frappe.model.document import Document


class FeaturedCourse(Document):
	pass


@frappe.whitelist(allow_guest=True)
def get_featured_courses():
    courses = []
    
    feat_courses = frappe.get_all("Featured Course", filters={'show_on_web': 1, "enabled": 1})
    
    if feat_courses:
        for feat_course in feat_courses:
            course = frappe.get_doc("Featured Course", feat_course.name)
            
            courses.append({
                "course_name": course.course_name,
                "course_image": course.course_image,
                "description": course.course_description,
            })
            
        frappe.response['messages'] = {
			'status': 1,
			'courses': courses
		}
        
    else:
        frappe.response['messages'] = {
			'status': 0,
			'error': 'No featured courses found'
		}
        
    return
    
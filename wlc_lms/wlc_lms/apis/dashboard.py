# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt
# Developed by Rino Ruth Ricardo

import frappe



@frappe.whitelist(allow_guest=True)
def get_featured_courses():
    courses = []
    
    feat_courses = frappe.get_all("Featured Course", filters={'show_on_web': 1, "enabled": 1}, order_by='creation asc')
    
    if feat_courses:
        for feat_course in feat_courses:
            course = frappe.get_doc("Featured Course", feat_course.name)
            
            courses.append({
                "course_id": course.course_id,
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

@frappe.whitelist(allow_guest=True)
def get_carousel_images():
    img_list = []
    
    img_doc_list = frappe.get_all("Carousel Images")
    
    
    if img_doc_list:
    
        for r in img_doc_list:
        
            img_doc = frappe.get_doc("Carousel Images", r.name)
            if img_doc:
                if img_doc.image_table:
                    for i in img_doc.image_table:
                        img_list.append(
                            i.image
                        )
                    frappe.response['messages'] = {
                        'status': 1,
                        'img_list': img_list
                    }
            else:    
                frappe.response['messages'] = {
                    'status': 0,
                    'error': 'No images found'
                }
    else:       
        frappe.response['messages'] = {
            'status': 0,
            'error': 'No doc found'
        }
    


@frappe.whitelist(allow_guest=True)
def get_why_wlc():
    whys_wlc = []
    
    whys = frappe.get_all("Why WLC", filters={'enabled': 1}, order_by="creation asc")
    
    if whys:
        for why in whys:
            why_wlc = frappe.get_doc("Why WLC", why.name)
            
            whys_wlc.append({
                "img": why_wlc.image,
                "title": why_wlc.title,
                "description": why_wlc.description,
            })
            
        frappe.response['messages'] = {
			'status': 1,
			'whys_wlc': whys_wlc
		}
        
    else:
        frappe.response['messages'] = {
			'status': 0,
			'error': 'No why WLC found'
		}
        
    return


@frappe.whitelist(allow_guest=True)
def get_dashboard():
    
    # featured courses 
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
    
    # the whys
    whys_wlc = []
    
    whys = frappe.get_all("Why WLC", filters={'enabled': 1})
    
    if whys:
        for why in whys:
            why_wlc = frappe.get_doc("Why WLC", why.name)
            
            whys_wlc.append({
                "img": why_wlc.image,
                "title": why_wlc.title,
                "description": why_wlc.description,
            })
    
    frappe.response['messages'] = {
        'status': 1,
        'courses': courses,
        'whys_wlc': whys_wlc
    }
    
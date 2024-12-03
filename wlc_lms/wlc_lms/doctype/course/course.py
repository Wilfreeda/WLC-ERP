# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt
# Developed by Rino Ruth Ricardo

import frappe
from frappe.model.document import Document
import frappe.utils


class Course(Document):
    def validate(self):
        # pass
        self.check_weightage()
        self.set_course_statistics()
    
    def check_weightage(self):
        if self.topic_table:
            weightage = 0.0
            for row in self.topic_table:
                if not row.weightage:
                    frappe.throw("The weightage for topic "+row.topic_name+" cannot be 0%")
                else:
                    weightage += row.weightage
            if weightage != 100.0:
                frappe.throw("The total weightage of all topics must be equal to 100%")
    
    def set_course_statistics(self):
        topics = 0
        
        if self.topic_table:
            for row in self.topic_table:
                topics += 1
        
        self.total_topics = topics


@frappe.whitelist(allow_guest = True)
def get_course_details(course_id):
    
    course = {}
    course_details = frappe.get_doc("Course", course_id)
    
    course_image_for_detailed_page = ''
    if course_details.course_image_2:
        course_image_for_detailed_page = course_details.course_image_2
        
    program_type = ''
    if course_details.program_type:
        program_type = course_details.program_type
        
    rating = 0
    if course_details.rating:
        rating = int((course_details.rating / 2) * 10)
        
    num_of_rating = 0
    if course_details.number_of_rating:
        num_of_rating = int(course_details.number_of_rating)
        
    skills = []
    if course_details.skills:
        for skill in course_details.skills:
            skills.append(skill.skill)
    
    why = {}
    if course_details.why:
        for i in course_details.why:
            why[i.title] = i.description
        
    reasons = {}
    if course_details.reasons:
        for i in course_details.reasons:
            reasons[i.title] = i.description
            
    c_structure = {}
    
    course_structure = frappe.get_all("Course Structure", {'course_name': course_id}, order_by='creation asc')
    if course_structure:
        for cs in course_structure:
            struct = frappe.get_doc("Course Structure", cs.name)
            if struct.structure_details:
                cs_list = []
                for sd in struct.structure_details:
                    cs_list.append(sd.structure_details)
                c_structure[struct.title] = cs_list
            
    
    
    
    course = {
        'course_name': course_id,
        'course_image': course_image_for_detailed_page,
        'program_type': program_type,
        'rating': rating,
        'no_rating': num_of_rating,
        'skills': skills,
        'why': why,
        'reasons': reasons,
        'course_structure': c_structure
    }
    
    frappe.response['messages'] = {
        'status': 1,
        'course': course
    }




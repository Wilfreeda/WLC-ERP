# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt
# Developed by Rino Ruth Ricardo

from __future__ import unicode_literals, print_function
import frappe
from frappe.utils import getdate
from frappe.model.document import Document


class Student(Document):
    def validate(self):
        self.full_name = ' '.join(filter(None, [self.first_name, self.last_name]))


@frappe.whitelist()
def create_student_user(doc, method=None):
    
    student_list = frappe.get_all("Student", filters={"mobile_no": doc.mobile_no}, fields={"name", "birth_date", "email"})
    today = getdate()
    
    if not student_list:
        student = frappe.get_doc({
			'doctype': 'Student',
			'first_name': doc.first_name,
			'last_name': doc.last_name,
			'email': doc.email,
			'birth_date': doc.birth_date,
			'mobile_no': doc.mobile_no,
			'gender': doc.gender,
			'student_status': 'Active',
			'date_of_registration': today
		})
        student.flags.ignore_permissions = True
        student.save()
        frappe.db.commit()
        
    else:
        for student in student_list:
            student = frappe.get_doc("Student", student.name)
            student.email = doc.email
            student.save()
            
@frappe.whitelist()
def set_student_status():
    # update the status of students daily
    student_list = frappe.get_all('Student', fields=['name', 'enrollment_status'])
    for student in student_list:
        enroll_list = frappe.get_all('Enrollment', filters={'student_id': student.name, 'enrollment_status': 'Actuve'})
        if enroll_list:
            frappe.db.set_value('Student', student.name, 'enrollment_status', 'Paid', update_modified=False)
            frappe.db.commit()
        else:
            frappe.db.set_value('Student', student.name, 'enrollment_status', 'Free', update_modified=False)
            frappe.db.commit()

@frappe.whitelist()
def set_single_student_status(student_id):
    # Update the status of student
    student = frappe.get_doc('Student', student_id)
    
    enroll_list = frappe.get_all('Enrollment', filters={'student_id': student.name, 'enrollment_status': 'Active'})
    if enroll_list:
        frappe.db.set_value('Student', student.name, 'enrollment_status', 'Paid', update_modified=False)
        frappe.db.commit()
    else:
        frappe.db.set_value('Student', student.name, 'enrollment_status', 'Free', update_modified=False)
        frappe.db.commit()
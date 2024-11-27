# Copyright (c) 2024, rino and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WLCStudentIntake(Document):
	pass


@frappe.whitelist(allow_guest=True)
# @frappe.validate_and_sanitize_search_inputs
def get_course_levels(course_name):
	checklist = []
	course_doc = frappe.get_doc('Course', course_name)
	if course_doc.levels:
		for level in course_doc.levels:
			checklist.append(level.level)

	print(f'\n\n\n{checklist}\n\n\n')
	return checklist
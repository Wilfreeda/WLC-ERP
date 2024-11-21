# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class StudentEnrollment(Document):
	def validate(self):
		lms_settings = frappe.get_doc("WLC LMS Settings")
		default_logo = lms_settings.default_image

		self.logo = default_logo


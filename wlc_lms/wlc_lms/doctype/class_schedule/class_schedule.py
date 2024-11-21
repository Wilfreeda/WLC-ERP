# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta


class ClassSchedule(Document):
	def validate(self):
		self.set_date_time()
		# self.validate_overlaps()
		# self.set_title()

	def set_date_time(self):
		start = datetime.strptime(self.class_from, "%Y-%m-%d %H:%M:%S")
		to = datetime.strptime(self.class_to, "%Y-%m-%d %H:%M:%S")

		duration = to - start

		hours = duration.total_seconds()

		self.duration = hours
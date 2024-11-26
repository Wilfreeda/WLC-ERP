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

		from_time = datetime.strptime(self.from_time, '%H:%M:%S')
		to_time = datetime.strptime(self.to_time, '%H:%M:%S')

		duration = (to_time - from_time).total_seconds()

		self.duration = duration
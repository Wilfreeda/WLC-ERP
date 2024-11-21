# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt, money_in_words, getdate
from frappe.model.document import Document


class StudentAdmission(Document):
	def validate(self):
		if self.product_id:
			self.calculate_fee()
			self.grand_total_in_words()
			self.set_payment_status()
		
	def calculate_fee(self):
		
		self.net_total = self.product_fee

		subtotal = flt(self.net_total)
		if self.provide_discounts:
			if flt(self.discount) < 0.0:
				frappe.throw("Discount cannot be negative")
			elif flt(self.discount) > self.net_total:
				frappe.throw("Discount cannot be greater than Net Total")
			else:
				subtotal = flt(self.net_total) - flt(self.discount)

		print(f'\n\n\n\n{subtotal}\n\n\n\n')

		self.grand_total_in_inr = flt(subtotal)


	def grand_total_in_words(self):
		self.grand_total_in_words_inr = money_in_words(self.grand_total_in_inr, main_currency = None, fraction_currency = None)


	def set_payment_status(self):
		if self.paid_amount == 0.0:
			self.payment_status = "Not Paid"
		elif self.balance_amount > 0.0:
			self.payment_status = "Partial Paid"
		elif self.balance_amount == 0.0:
			self.payment_status = "Fully Paid"
	
	# def create_invoice(self):
	# 	student = frappe.get_doc("Student", self.student_id)

	# 	course = frappe.get_doc("Course", self.product_id)
	# 	course_fee = flt(self.grand_total)

	# 	if course_fee < 0.0:
	# 		course_fee = 0.0
		
	# 	if course.fee_components:
	# 		pass

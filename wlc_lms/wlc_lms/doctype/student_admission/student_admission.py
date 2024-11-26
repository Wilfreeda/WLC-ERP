# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt, money_in_words, getdate
from frappe.model.document import Document


class StudentAdmission(Document):
	# def after_insert(self):
	# 	self.set_payment_status()
	def validate(self):
		if self.course_item_id:
			self.calculate_fee()
			self.grand_total_in_words()
			self.set_trasactions()
			self.set_payment_status()
		
	def calculate_fee(self):
		
		# self.net_total = self.course_fee

		subtotal = flt(self.net_total)
		if self.provide_discounts:
			if flt(self.discount) < 0.0:
				frappe.throw("Discount cannot be negative")
			elif flt(self.discount) > self.net_total:
				frappe.throw("Discount cannot be greater than Net Total")
			else:
				subtotal = flt(self.net_total) - flt(self.discount)

		self.grand_total_in_inr = flt(subtotal)
		self.balance_amount = flt(self.grand_total_in_inr) - flt(self.paid_amount)


	def grand_total_in_words(self):
		self.grand_total_in_words_inr = money_in_words(self.grand_total_in_inr, main_currency = None, fraction_currency = None)


	def set_payment_status(self):
		if self.paid_amount == 0.0:
			print("\n\n\n\nNot Paid\n\n\n\n")
			self.payment_status = "Not Paid"
		elif self.balance_amount > 0.0:
			print("\n\n\n\nPart Paid\n\n\n\n")
			self.payment_status = "Partial Paid"
		elif self.balance_amount <= 0.0 or (self.paid_amount == self.grand_total_in_inr):
			print("\n\n\n\nFully Paid\n\n\n\n")
			self.payment_status = "Fully Paid"

	def set_trasactions(self):
		paid_amount = flt(self.paid_amount)
		paid_transaction = 0.0
		if self.table_transactions:
			for transactions in self.table_transactions:
				if transactions.paid_amount:
					paid_transaction += flt(transactions.paid_amount)
					# self.balance_amount = flt(self.balance_amount) - flt(self.paid_amount)
		
		self.balance_amount = flt(self.grand_total_in_inr) - flt(paid_transaction)
		self.paid_amount = paid_transaction

	
	# def create_invoice(self):
	# 	student = frappe.get_doc("Student", self.student_id)

	# 	course = frappe.get_doc("Course", self.product_id)
	# 	course_fee = flt(self.grand_total)

	# 	if course_fee < 0.0:
	# 		course_fee = 0.0
		
	# 	if course.fee_components:
	# 		pass

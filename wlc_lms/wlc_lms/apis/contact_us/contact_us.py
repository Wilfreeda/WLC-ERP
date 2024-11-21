import frappe
from frappe.utils import escape_html, now


@frappe.whitelist(allow_guest=True)
def submit_enquiry(name, email, msg):

    print(f'\n\n\n\n{name}, {email}, {msg}\n\n\n')
    inqury = frappe.get_doc({
        'doctype': 'WLC Enquires',
        'name1': escape_html(name),
        'email_address': escape_html(email),
        'message': escape_html(msg),
        'date_time': now()
    })
    inqury.flags.ignore_permissions = True
    inqury.save()
    frappe.db.commit()
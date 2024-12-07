
import frappe

@frappe.whitelist(allow_guest=True)
def create_demo_doc(name, email, phone, time_slot, course, selected_date):

    print(f'\n\n\n\n{course}\n\n\n\n')
    doc = frappe.get_doc({
        'doctype': 'Demo Request',
        'name1': name,
        'email': email,
        'mobile_no': phone,
        'time_slot': time_slot,
        'course': course,
        'selected_date': selected_date
    })
    doc.flags.ignore_permissions = True
    doc.insert()
    frappe.db.commit()

    frappe.response['messages'] = {
        'status': 1,
        'message': 'Demo Request created successfully'
    }

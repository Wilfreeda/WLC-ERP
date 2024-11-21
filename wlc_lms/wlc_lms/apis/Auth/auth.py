# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt
# Developed by Rino Ruth Ricardo


# this files contains all the apis that uses in the authentication parts


import frappe
from frappe.utils import escape_html
import math, random
from frappe.auth import LoginManager, get_logged_user
import frappe.utils
from frappe.utils.password import get_decrypted_password




@frappe.whitelist(allow_guest=True)
def sign_in(username, password):
    try:
        login_manager = LoginManager()
        login_manager.authenticate(user=username, pwd=password)
        login_manager.post_login()
    
    except frappe.exceptions.SecurityException:
        frappe.clear_messages()
        frappe.response["message"] = {
			"status_key": 0,
			"message": "Your account has been locked for 5 minutes."
		}
        return
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.response["message"] = {
			"status_key": 0,
			"message": "Invalid username or password........"
		}
        return
    
    api_generate = generate_keys(frappe.session.user)
    
    roles = frappe.get_roles()
    student = False
    for role in roles:
        if role == "Student":
            student = True
        
        break
    if student:
        client = frappe.get_doc("Student", {"email": frappe.session.user})
        user = frappe.get_doc("User", frappe.session.user)
        user = frappe.get_doc('User', user.name)

        api_secret = get_decrypted_password("User", user.name, fieldname="api_secret")
        
        profile_pic = ""
        if user.user_image:
            profile_pic = 'http://localhost:8000' + str(frappe.utils.get_files_path(user.user_image))
        
        frappe.clear_messages()
        frappe.response["message"] = {
			"status_key": 1,
			"message": "Login Successful",
			"first_name": user.first_name,
			"last_name": user.last_name,
			'candidate_id': client.name,
			'api_key': user.api_key,
			'api_secret': api_secret,
            'profile_pic': profile_pic
		}
    else:
        frappe.clear_messages()
        frappe.response["message"] = {
			"status_key": 0,
			"message": "You are not authorized to access this page."
		}

def generate_keys(user):
	user = frappe.get_doc("User", user)
	api_secret = frappe.generate_hash(length=25)
	if not user.api_key:
		api_key = frappe.generate_hash(length=25)
		user.api_key = api_key
	user.api_secret = api_secret
	user.save(ignore_permissions=True)



@frappe.whitelist(allow_guest=True)
def check_user(email, mobile_no, first_name):
    
    email_id = frappe.db.get("User", {'email': email})
    mobile = frappe.db.get("User", {'mobile_no': mobile_no})
    
    if email_id and mobile:
        frappe.local.response['message'] = {
            "status": 0,
            'message': "User is already registered"
        }
    elif email_id:
        frappe.response['message'] = {
            "status": 0,
            "message": "This email is already registed"
        }
    elif mobile:
        frappe.response['message'] = {
            "status": 0,
            "message": "This mobile number is already registered"
        }
    else:
        digits = "0123456789"
        
        OTP = ""
        for i in range(4):
            OTP = digits[math.floor(random.random() * 10)]
        
        number = ""
        for i in range(3):
            number = digits[math.floor(random.random() * 3)]
            
        unique_id = number + '_' + mobile_no
        time_in_sec = 180
        frappe.cache().set_value(unique_id, OTP, expires_in_sec=time_in_sec)
        
        #sending email
        # message = "Dear {0},<br><br>".format(first_name)
        # message += "Thank you for signing up with Wilfreeda's Language Centre!<br>"
        # message += "YTo complete your registration, please enter the following verification code: <br><br>"
        # message += "<b>{0}</b><br><br>".format(OTP)
        # message += "This code is unique to your account and should not be shared with anyone.<br><br>"
        # message += "Please note: This code will expire in {0} minutes.".format(time_in_sec/60)
        # message += "If you did not request this verification code or have any questions, please contact our support team at enquiries@wilfreedas.com<br><br>"
        # message += "Sincerely,<br>"
        # message += "The Wilfreeda's Language Centre Team"
        
        
        # frappe.sendmail(
        #     recipients = email,
        #     subject = "Wilfreeda's Language Centre - Email Verification",
        #     message = message,
        #     now = True
        # )
        
        frappe.response["message"] = {
            "status": 1,
            "message": "User does not exist. OTP sent",
            "unique_id": unique_id
        }
        
        
@frappe.whitelist(allow_guest=True)
def sign_up(email, mobile_no, password, first_name, last_name, gender, birth_date):
    
    
    email_id = frappe.db.get("User", {'email': email})
    mobile = frappe.db.get("User", {'mobile_no': mobile_no})
    
    if email_id and mobile:
        frappe.response['message'] = {
            "status": 0,
            'message': "User is already registered."
        }
        return
    elif email_id:
        frappe.response['message'] = {
            "status": 0,
            "message": "This email is already registed."
        }
        return
    elif mobile:
        frappe.response['message'] = {
            "status": 0,
            "message": "This mobile number is already registered."
        }
        return
    else:
        if len(mobile_no) != 10:
            frappe.response['message'] = {
                "status": 0,
                "message": "Mobile number should have at least 10 digits."
            }
            return
        if len(password) < 8:
            frappe.response['message'] = {
                "status": 0,
                "message": "Password should be at least 8 characters."
            }
            return
        elif not gender in ['Male', 'Female', 'Other']:
            frappe.response['message'] = {
                "status": 0,
                "message": "Invalid gender."
            }
            return
        else:
            
            
            user = frappe.get_doc({
                'doctype': 'User',
                'email': email,
                'first_name': escape_html(first_name),
                'last_name': escape_html(last_name),
                'gender': escape_html(gender),
                'birth_date': birth_date,
                'mobile_no': mobile_no,
                'enabled': 1,
                'send_welcom_email': 0,
                'send_password_update_notification': 0,
                'user_type': "Website User"
            })
            user.flags.ignore_permissions = True
            user.flags.ignore_password_policy = True
            user.insert()
            user.new_password = password
            user.save()
            
            default_role = frappe.db.get_value('Portal Settings', None, 'default_role')
            if default_role:
                user.add_roles(default_role)
            
            frappe.db.commit()
            
            
            frappe.response['message'] = {
                "status": 1,
                "message": "User registered successfully."
            }
            
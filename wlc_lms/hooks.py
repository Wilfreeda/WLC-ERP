app_name = "wlc_lms"
app_title = "WLC LMS"
app_publisher = "rino"
app_description = "an app for the lms"
app_email = "admin@wlc.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "wlc_lms",
# 		"logo": "/assets/wlc_lms/logo.png",
# 		"title": "WLC LMS",
# 		"route": "/wlc_lms",
# 		"has_permission": "wlc_lms.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wlc_lms/css/wlc_lms.css"
# app_include_js = "/assets/wlc_lms/js/wlc_lms.js"

# include js, css files in header of web template
# web_include_css = "/assets/wlc_lms/css/wlc_lms.css"
# web_include_js = "/assets/wlc_lms/js/wlc_lms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "wlc_lms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "wlc_lms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "wlc_lms.utils.jinja_methods",
# 	"filters": "wlc_lms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "wlc_lms.install.before_install"
# after_install = "wlc_lms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "wlc_lms.uninstall.before_uninstall"
# after_uninstall = "wlc_lms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "wlc_lms.utils.before_app_install"
# after_app_install = "wlc_lms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "wlc_lms.utils.before_app_uninstall"
# after_app_uninstall = "wlc_lms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wlc_lms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "User": {
        "after_insert": "wlc_lms.wlc_lms.doctype.student.student.create_student_user"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wlc_lms.tasks.all"
# 	],
# 	"daily": [
# 		"wlc_lms.tasks.daily"
# 	],
# 	"hourly": [
# 		"wlc_lms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wlc_lms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"wlc_lms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "wlc_lms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wlc_lms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wlc_lms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["wlc_lms.utils.before_request"]
# after_request = ["wlc_lms.utils.after_request"]

# Job Events
# ----------
# before_job = ["wlc_lms.utils.before_job"]
# after_job = ["wlc_lms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"wlc_lms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


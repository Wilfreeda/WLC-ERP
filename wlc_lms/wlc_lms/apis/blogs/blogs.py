# Copyright (c) 2024, WLC. and contributors
# For license information, please see license.txt
# Developed by Rino Ruth Ricardo


import frappe

@frappe.whitelist(allow_guest=True)
def get_blogs_list():

    blogs = []

    blog_list = frappe.get_all("Blogs WLC", filters={'enabled': 1, 'show_on_website': 1}, order_by='creation asc')

    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_image = str(lms_settings.hostname) + str(lms_settings.default_image)

    if blog_list:

        for blog in blog_list:
            blog_doc = frappe.get_doc("Blogs WLC", blog.name)

            if blog_doc.blog_image:
                image = str(lms_settings.hostname) + blog_doc.blog_image
            else:
                image = default_image

            blogs.append({
                "blog_id": blog_doc.name,
                "title": blog_doc.blog_title,
                "image": image,
            })

        frappe.response['messages'] = {
            'status': 1,
            'blogs': blogs
        }

    else:
        frappe.response['messages'] = {
            'status': 0,
            'message': 'No blogs found'
        }


@frappe.whitelist(allow_guest=True)
def get_blog_details(blog_id):

    blog_details = []

    blog = frappe.get_doc("Blogs WLC", blog_id)
    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_image = str(lms_settings.hostname) + str(lms_settings.default_image)

    if blog.blog_image:
        image = str(lms_settings.hostname) + blog.blog_image
    else:
        image = default_image

    blog_details.append({
        "title": blog.blog_title,
        "image": image,
        "description": blog.blog_content,
    })

    frappe.response['messages'] = {
        'status': 1,
        'blog_details': blog_details
    }
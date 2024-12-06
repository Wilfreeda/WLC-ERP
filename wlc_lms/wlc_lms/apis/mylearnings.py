

import frappe
from frappe.auth import get_logged_user
from frappe.utils import getdate
from datetime import datetime

@frappe.whitelist()
def get_enrollments():
    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_logo = str(lms_settings.hostname) + str(lms_settings.default_image)

    token_user = get_logged_user()
    student = frappe.get_doc("Student", {"email": token_user})
    doc = frappe.get_doc('Student', student.name)

    enrollment_list = frappe.get_all('Student Enrollment', filters={'student_id': doc.name})
    
    my_courses = []
    if enrollment_list:
        for enrollments in enrollment_list:
            enrollment = frappe.get_doc('Student Enrollment', enrollments.name)
            course = frappe.get_doc('Course', enrollment.course_name)

            if course.course_image:
                course_image = str(lms_settings.hostname) + str(course.course_image)
            else:
                course_image = default_logo

            educator = frappe.get_doc('Educator', enrollment.educator)
            
            my_courses.append({
                'course_name': course.name,
                'enrollment_id': enrollment.name,
                'course_image': course_image,
                'educator': educator.full_name,
                'rating': course.rating,
                'course_description': course.course_description,
                # 'course_duration': course.course_duration,
                'course_start_date': enrollment.activation_date,
                # 'course_end_date': enrollment.end_date,
                'course_status': enrollment.enrollment_status
            })

        frappe.response["message"] = {
            "status": 1,
            "message": "Enrollments fetched successfully",
            "my_courses": my_courses
        }
    else:
        frappe.response["message"] = {
            "status": 0,
            "message": "No enrollments found"
        }


@frappe.whitelist()
def get_enrollment(enrollment_id):
    lms_settings = frappe.get_doc("WLC LMS Settings")
    default_logo = str(lms_settings.hostname) + str(lms_settings.default_image)

    today = getdate()

    token_user = get_logged_user()
    student = frappe.get_doc("Student", {"email": token_user})
    doc = frappe.get_doc('Student', student.name)

    enrollment = frappe.get_doc('Student Enrollment', enrollment_id)

    class_schedules = frappe.get_all('Class Schedule', filters={'enrollment_id': enrollment.name, 'class_status': "Scheduled"})

    todays_activity = []

    for class_schedule in class_schedules:
        class_schedule = frappe.get_doc('Class Schedule', class_schedule.name)

        activity_name = ""
        if class_schedule.schedules_topics:
            for topics in class_schedule.schedules_topics:
                activity_name = str(topics.sub_course) + " - " + str(topics.topic)

        trainer = class_schedule.educator_name

        date_obj = datetime.strptime(str(class_schedule.class_date), '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d %b')

        from_time_obj = datetime.strptime(str(class_schedule.from_time), '%H:%M:%S')
        formatted_from_time = from_time_obj.strftime('%I%p').lower()

        to_time_obj = datetime.strptime(str(class_schedule.to_time), '%H:%M:%S')
        formatted_to_time = to_time_obj.strftime('%I%p').lower()


        time = '(' + formatted_from_time + ' - ' + formatted_to_time + ' IST)'

        sch = str(formatted_date) + " " + str(time)

        if class_schedule.class_status == "Scheduled" and class_schedule.class_date == today:
            todays_activity.append({
                'class_date': class_schedule.class_date,
                'activity': activity_name,
                "trainer": trainer,
                "schedule": sch,
                'duration': str(class_schedule.duration / 3600) + str(" Hrs."),
                'class_status': class_schedule.class_status,
                'class_link': class_schedule.class_link
            })


    past_schedules = frappe.get_all('Class Schedule', filters={'enrollment_id': enrollment.name, 'class_status': "Class Completed"})

    past_schedule = []
    progressed_duration = 0
    for pSchedules in past_schedules:
        schedule = frappe.get_doc('Class Schedule', pSchedules.name)
        if schedule.duration:
            duration = schedule.duration / 3600
            progressed_duration += duration

        if schedule.schedules_topics:
            for topics in schedule.schedules_topics:
                activity_name = str(topics.sub_course) + " - " + str(topics.topic)

        past_schedule.append({
            'activity': activity_name,
            'class_date': schedule.class_date,
            "trainer": schedule.educator_name,
            'class_status': schedule.class_status,
        })

    if enrollment.course_duration:
        course_duration = int(enrollment.course_duration)

    
    progress = int((progressed_duration / course_duration) * 100)



    frappe.response['messages'] = {
        'status': 1,
        'message': 'Class schedules fetched successfully',
        'past_schedules': past_schedule,
        'todays_activity': todays_activity,
        'progress': progress
        # 'enrollment': enrollment,
        # 'course_image': default_logo
    }
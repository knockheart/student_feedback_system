from django.urls import path

from api_service.views import get_list_of_feedbacks_for_professor, get_list_of_feedbacks_from_student, get_user_profile, \
    get_user_profile_by_email, post_feedback, get_all_professors, add_student, get_all_branch, get_all_college, \
    update_student, get_all_subjects, get_all_semester

urlpatterns = [
    path("professor/feedback/professor_id/<professor_id>", get_list_of_feedbacks_for_professor),
    path("professor/all", get_all_professors),

    path("profile/<user_type>/<user_id>", get_user_profile),
    path("profile/email/<user_type>/<email_id>", get_user_profile_by_email),

    path("student/student_id/<student_id>", get_list_of_feedbacks_from_student),
    path("student/feedback", post_feedback),
    path("student/add", add_student),
    path("student/update", update_student),

    path("branch/all", get_all_branch),
    path("college/all", get_all_college),
    path("subject/all", get_all_subjects),
    path("semester/all", get_all_semester),

]

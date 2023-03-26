from django.urls import path

from api_service.views import get_list_of_feedbacks_for_professor, get_list_of_feedbacks_from_student, get_user_profile, \
    get_user_profile_by_email, post_feedback, get_all_professors

urlpatterns = [
    path("professor/professor_id/<professor_id>", get_list_of_feedbacks_for_professor),
    path("professor/all", get_all_professors),

    path("profile/<user_type>/<user_id>", get_user_profile),
    path("profile/email/<user_type>/<email_id>", get_user_profile_by_email),

    path("student/student_id/<student_id>", get_list_of_feedbacks_from_student),
    path("student/feedback", post_feedback),

]

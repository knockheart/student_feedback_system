from django.urls import path

from feedback.views import StudentMainPage, custom_logout

urlpatterns = [

    # path("login/", LoginFormView.as_view(), name='student_login'),
    path("s_main/", StudentMainPage.as_view()),
    path("logout/", custom_logout),
]

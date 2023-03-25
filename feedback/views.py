from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from passlib.hash import django_pbkdf2_sha256

from feedback.forms import FeedbackRequest
from feedback.models import FeedbackItems, Feedback
from users.models import Admin


class StudentMainPage(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    # redirect_field_name = '/feedback/s_main'
    template_name = 'student/student_main_page_dashboard.html'

    # @method_decorator(login_required(login_url='/admin/login'))
    def get(self, request, *args, **kwargs):
        print()
        print(request.__dict__.keys())
        print("user", request.__dict__["_cached_user"])
        print("user", request.__dict__["user"])
        print(request.__dict__["environ"]["QUERY_STRING"])
        # print(json.dumps(request.__dict__, default=lambda x: "", indent=4))
        print(args, kwargs)

        query_string = request.__dict__["environ"]["QUERY_STRING"]
        user_email = request.__dict__["user"]

        user_object = Admin.objects.get(email=user_email)

        if query_string and query_string.lower() == "feedback":
            feedback_items = FeedbackItems.objects.all()
            context = {
                "email": user_object.email,
                "feedback_items": feedback_items,
                "feedback_item_total_count": len(feedback_items),
            }
            return render(request, "student/student_main_page_feedback.html", context)
        elif query_string and query_string.lower() == "profile":
            print(user_object.__dict__)
            context = {"user": user_object}
            return render(request, "student/student_main_page_profile.html", context)
        elif query_string and query_string.lower() == "logout":
            return render(request, "student/student_main_page_logout.html")
        else:
            feedback_items = FeedbackItems.objects.all()
            feedbacks = Feedback.objects.filter(user=user_object)
            context = {
                "feedback_items": feedback_items,
                "feedbacks": feedbacks,
                "feedback_item_total_count": len(feedback_items),
            }
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        query_string = request.__dict__["environ"]["QUERY_STRING"]
        user_email = request.__dict__["user"]

        user_object = Admin.objects.get(email=user_email)

        if query_string and query_string.lower() == "feedback":
            print("POST")
            print("Feedback")

            # print(feedback_request.__dict__)
            # print()
            #
            # print(feedback_request.__dict__["data"])
            # print()

            feedback_items = FeedbackItems.objects.all()

            context = {
                "email": user_object.email,
                "feedback_items": feedback_items,
                "feedback_item_total_count": len(feedback_items),
                "create_message": True,
            }
            feedback_request = FeedbackRequest(request.POST)

            if feedback_request.is_valid():
                print("valid")
                print(feedback_request.__dict__["data"])
                form_data = feedback_request.__dict__["data"]
                user_object = Admin.objects.get(email=form_data["feedback_request_email"])
                feedback_items = FeedbackItems.objects.get(title=form_data["feedback_request_item"])
                feed_back = Feedback(
                    feedback_items=feedback_items,
                    rating=form_data["feedback_request_rating"],
                    message=form_data["feedback_request_message"],
                    user=user_object
                )
                feed_back.save()
                context["error_message"] = False
                context["create_message"] = True
            else:
                context["error_message"] = True
                context["create_message"] = False

            return render(request, "student/student_main_page_feedback.html", context)


# class LoginFormView(View):
#     form_class = LoginForm
#     template_name = 'login.html'
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)
#
#     def post(self, request, *args, **kwargs):
#         print("xxx => ", args, kwargs)
#         form = self.form_class(request.POST)
#         errors = ""
#         if form.is_valid():
#             print()
#             print(form.__dict__)
#             print(form.__dict__["data"]["login_email"], form.__dict__["data"]["login_password"])
#             login_email = form.__dict__["data"]["login_email"]
#             login_password = form.__dict__["data"]["login_password"]
#
#             try:
#                 user: Admin = Admin.objects.get(email=login_email)
#                 print("user", user)
#                 print(user.password)
#                 is_valid = django_pbkdf2_sha256.verify(login_password, user.password)
#                 if is_valid:
#                     print("User is valid")
#                     return HttpResponseRedirect('/feedback/s_main/')
#                     # return redirect('/feedback/s_main/')
#                 else:
#                     raise Exception("Invalid Password")
#             except Admin.DoesNotExist as does_not_exist:
#                 print(does_not_exist)
#                 errors = form.__dict__["_errors"]
#             except Exception as exception:
#                 print(exception)
#                 errors = "Invalid credentials"
#
#         else:
#             print(form.__dict__["_errors"])
#             errors = form.__dict__["_errors"]
#
#         print("error => ", errors)
#         return render(request, self.template_name, {"login_error": errors})


def custom_logout(request):
    print('Loggin out {}'.format(request.user))
    auth.logout(request)
    print(request.user)
    return HttpResponseRedirect('/feedback/s_main')

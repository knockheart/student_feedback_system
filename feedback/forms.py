from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#
# class LoginForm(forms.Form):
#     login_email = forms.EmailField(label="email")
#     login_password = forms.PasswordInput()


class FeedbackRequest(forms.Form):
    feedback_request_email = forms.EmailField()
    feedback_request_item = forms.CharField()
    feedback_request_rating = forms.CharField()
    feedback_request_message = forms.CharField()

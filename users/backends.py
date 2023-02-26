import logging

from django.contrib.auth.backends import ModelBackend

from users.models import CustomUser as UserModel


class MyAuthBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        print("Auth...........................................................")
        print(kwargs)
        email = kwargs.get('username', None)
        password = kwargs.get('password', None)
        try:
            print(email, password)
            if email and password:
                user = UserModel.objects.get(email=email)
                if user.check_password(password) is True:
                    return user
            return None
        except UserModel.DoesNotExist as login:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

from django.contrib.auth.models import User

# authenticates the user by matching both email and password
class EmailAuth:

    def authenticate(self, username=None, password=None):

        # get an instance of 'User' based off email and verified password
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):

        # Django authentication system retrieves the user instance
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None
from user.models import base as base_user_models
from helper import keys
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken



class TokenFunction:
    def generate_token(user):
        
        response = {}
        refresh = RefreshToken.for_user(user)
        response[keys.REFRESH] = str(refresh)
        response[keys.ACCESS] = str(refresh.access_token)
        return response

class UserFunctions:

    def validate_user(**filter_dict):
        try:
            if base_user_models.User.objects.filter(email=filter_dict[keys.EMAIL]).exists():
                user =  base_user_models.User.objects.get(email=filter_dict[keys.EMAIL])
                if check_password(filter_dict[keys.PASSWORD], user.password):
                    response_json = TokenFunction.generate_token(user)
                    return {
                        keys.STATUS:True,
                        keys.RESPONSE:response_json
                    }
                else:
                    return {
                        keys.STATUS:False,
                        keys.MESSAGE:'invalid cred'
                    }
            else:
                return {
                        keys.STATUS:False,
                        keys.MESSAGE:'invalid cred'
                    }
        except Exception as e:
            return {
                        keys.STATUS:False,
                        keys.MESSAGE:str(e)
                    }


    def remove_space(arg):
        return ''.join(list(map(lambda x: x.strip(),arg.split())))

import base64
from django.contrib.auth.models import update_last_login, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

class TokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data['refresh'] = str(refresh)

        res = {
            "code": 20000,
            "data": data
        }
        return res


class TokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = str(self.user.username)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        res = {
            "code": 20000,
            "data": data
        }
        return res


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenViewBase):
    serializer_class = TokenRefreshSerializer


# 实现接口/vue-element-admin/user/info 进行用户信息和权限的设置
class userInfoView(APIView):
    def get(self, request):
        token = request.query_params.get("token")
        token_strings = token.split('.')
        # 得到该登录用户的id,并从auth_user表中筛选出此用户
        user_id = eval(str(base64.b64decode(token_strings[1]), 'utf8'))['user_id']
        User.objects.filter(id=user_id).first()[0]
        if token == "admin-token":
            roles = ["admin"]

        else:
            roles = ["editor"]

        response = {
            "code": 20000,
            "data": {
                "roles": roles,
                "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            }
        }
        return Response(response)


# 实现接口/vue-element-admin/user/logout 登出
class logoutView(APIView):
    def post(self, request):
        response = {
            "code": 20000,
            "data": "success"
        }
        return Response(response)

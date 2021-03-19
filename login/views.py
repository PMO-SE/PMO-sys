from rest_framework.views import APIView
from rest_framework.response import Response
from login import models


# 实现接口/vue-element-admin/user/login 进行密码校验
class loginView(APIView):

    def post(self, request, *args, **kwargs):
        users = models.User.objects.all()
        username = request.data.get("username")
        password = request.data.get("password")
        flag = 1
        for user in users:
            print(user.username, user.password)
            if user.username == username and user.password == password:
                flag = 0
                if user.identity == 'admin':
                    token = "admin-token"
                    # token = obtain_jwt_token
                elif user.identity == 'editor':
                    token = "editor-token"
                elif user.identity == 'visitor':
                    token = "visitor-token"
                elif user.identity == 'Tan':
                    token = "Tan-token"
                elif user.identity == 'Laura':
                    token = "Laura-token"
                elif user.identity == 'Eric':
                    token = "Eric-token"
                elif user.identity == 'Peggy':
                    token = "Peggy-token"
                else:
                    token = "no-token"
                response = {
                    "code": 20000,
                    "data": {"token": token}
                }
        if flag == 1:
            response = {
                "code": 60204,
                "msg": "No such person"
            }
        return Response(response)


# 实现接口/vue-element-admin/user/info 进行用户信息和权限的设置
class userInfoView(APIView):
    def get(self, request):
        token = request.query_params.get("token")
        if token == "admin-token":
            roles = ["admin"]
        elif token == "editor-token":
            roles = ["editor"]
        elif token == "Tan-token":
            roles = ["admin"]
        elif token == "Laura-token":
            roles = ["editor"]
        elif token == "Eric-token":
            roles = ["editor"]
        elif token == "Peggy-token":
            roles = ["editor"]
        else:
            roles = ["visitor"]

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


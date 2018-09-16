from users.models import Users
from users.serializers import UserSerializer
from kauth.auth import ExpiringTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.http import JsonResponse as json_response
# Create your views here.

auth = ExpiringTokenAuthentication()

@api_view(['POST'])
def login_views(request):
    receive = request.data
    if request.method == 'POST':
        username = receive['username']
        password = receive['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # update the token
            token = Token.objects.get(user=user)
            token.delete()
            token = Token.objects.create(user=user)
            user_info = Users.objects.get(user=user)
            serializer = UserSerializer(user_info)

            response = serializer.data
            response['token'] = token.key

            return json_response({
                "result": 1,
                "user_info":response, # response contain user_info and token
                })
        else:
            try:
                Users.objects.get(username=username)
                cause = u'密码错误'
            except Users.DoesNotExist:
                cause = u'用户不存在'

            return json_response({
                "result": 0,
                "cause":cause,
                })

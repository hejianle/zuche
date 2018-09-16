from rest_framework.serializers import ModelSerializer
from users.models import Users

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fileds = ('name', 'openid', 'token', 'sex')
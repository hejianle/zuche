from rest_framework.serializers import ModelSerializer
from ..users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fileds = ('nick_name', 'gender', 'language', 'country',
                  'province', 'city', 'open_id', 'avatar_url', 'register_date')
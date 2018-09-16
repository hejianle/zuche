from rest_framework.serializers import ModelSerializer
from users.models import Users

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fileds = ('nick_name', 'gender', 'language', 'country',
                  'province', 'city', 'open_id', 'avatar_url', 'register_date')
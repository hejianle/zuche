# Create your views here.
import requests
from django.core.cache import cache
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from wxutils import WXBizDataCrypt
from wxutils.django_jwt_session_auth import jwt_login
from users.models import User, Bicycle
from utils.cache_utils import redis_cache

appid = 'wxd8f471f80a7122e4'
app_secret = 'ab66ea663c909a770b00d686ae0b51e8'


def login(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        iv = request.POST.get('iv', '')
        encrypted_data = request.POST.get('encryptedData', '')

        session_info = get_session_info(appid, app_secret, code)
        session_key = session_info['session_key']

        crypt = WXBizDataCrypt(appid, session_key)
        user_info = crypt.decrypt(encrypted_data, iv)
        open_id = user_info['openId']
        try:
            user = User.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            user = register(user_info)
        token = jwt_login(user, request)
        user_info['token'] = token.decode()
        redis_cache.cache_token(user_info['token'], open_id)
        print(user_info)
        return JsonResponse(user_info)


def register(user_info):
    user = User(nick_name=user_info['nickName'], gender=user_info['gender'],
                language=user_info['language'], country=user_info['country'],
                province=user_info['province'], city=user_info['city'],
                open_id=user_info['openId'], avatar_url=user_info['avatarUrl'])
    user.save()


def get_session_info(code, appid, secret):
    base_url = "https://api.weixin.qq.com/sns/jscode2session?"
    query_obj = {}
    query_obj['appid'] = appid
    query_obj['secret'] = secret
    query_obj['js_code'] = code
    query_obj['grant_type'] = 'authorization_code'

    response = requests.get(base_url, params=query_obj)
    data = response.json()
    return data


def rent_bicycle(request):

    bicycle_id = request.data.get('bicycle_id')
    open_id = request.data.get('open_id')

    if not cache.hget(bicycle_id, open_id):
        end_time = request.data.get("end_time")
        cost = (end_time - cache.hget(bicycle_id, open_id)) * 1


    else:
        cache.hput(bicycle_id, open_id, request.data.get('start_time'))
        return 'successfully!'

from django.core.cache import cache

class TokenCache(object):
    def __init__(self):
        self.cache = cache


    def cache_token(self, token, openid, expire=None):
        key = "token".join(":", token)
        openid_in_cache = self.cache.get(key)
        if not openid_in_cache or openid != openid_in_cache:
            self.cache.set(key, openid, expire=expire)

    def validate_token(self, token):
        key = "token".join(":", token)
        openid = self.cache.get(key)
        if openid:
            return openid
        else:
            return False

redis_cache = TokenCache()



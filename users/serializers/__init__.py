from .auth import AuthSerializer
from .user import UserDetails


class UserSerializer:
    class Auth(AuthSerializer):
        pass

    class User(UserDetails):
        pass

import jwt
from datetime import datetime, timedelta
import secrets
import string

# 사용자 정보를 받아 로그인 처리하는 함수
def login(user):
    # 정해진 유저네임과 패스워드 리스트를 정의합니다.
    allowed_users = [
        {"username": "sc22", "password": "falinux"},
        # 여기에 다른 유저 정보를 추가할 수 있습니다.
    ]

    # print ("user.username", user.username)
    # print ("user.password", user.password)

    # 입력된 유저네임과 패스워드를 확인하여 인증을 처리합니다.
    for allowed_user in allowed_users:
        if user.username == allowed_user["username"] and user.password == allowed_user["password"]:
            # 로그인 성공 시, 토큰을 생성하여 리턴합니다.
            token = generate_token(user.username)
            return {"auth": True, "token": token}

    # 로그인 실패 시, 인증 실패 메시지를 리턴합니다.
    return {"auth": False, "message": "Authentication failed"}

def generate_random_key(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_key = ''.join(secrets.choice(characters) for _ in range(length))
    return random_key

# 토큰 생성 함수
def generate_token(username: str):
    # 토큰의 만료 시간을 정의합니다. 여기서는 1시간으로 설정하겠습니다.
    expires = datetime.utcnow() + timedelta(hours=1)
    
    # 토큰 페이로드를 정의합니다.
    payload = {
        'username': username,
        'exp': expires
    }
    
    # 토큰을 생성하여 리턴합니다.
    # 32자리의 무작위 비밀 키 생성
    secret_key = generate_random_key(32)
    print(secret_key)

    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token
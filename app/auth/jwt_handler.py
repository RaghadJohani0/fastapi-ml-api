from jose import jwt

SECRET = "secret"


def create_token(data):

    token = jwt.encode(
        data,
        SECRET
    )

    return token

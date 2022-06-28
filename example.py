from dataclasses import asdict
from firebaseauth_py import FirebaseAuthClient
from firebaseauth_py.errors import ErrorResponse
from firebaseauth_py.firebase_auth import SignUpResponse


def main():
    email = ""
    password = ""
    api_key = ""
    client = FirebaseAuthClient(api_key)
    res = client.sign_up(email, password)

    if isinstance(res, ErrorResponse):
        # TODO: handle error
        print(asdict(res))
    else:
        assert isinstance(res, SignUpResponse), "should be a SignUpResponse instance"
        print(asdict(res))


if __name__ == "__main__":
    main()

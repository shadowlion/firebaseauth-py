from dataclasses import asdict
from firebaseauth_py import FirebaseAuthClient
from firebaseauth_py.errors import ErrorResponse


def main():
    email = ""
    password = ""
    api_key = ""
    client = FirebaseAuthClient(api_key)
    res = client.sign_in_with_password(email, password)

    if isinstance(res, ErrorResponse):
        # TODO: handle error
        print(asdict(res))
    else:
        print(asdict(res))


if __name__ == "__main__":
    main()

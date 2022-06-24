from dataclasses import asdict

from firebaseauth_py import FirebaseAuthClient


def main():
    email = ""
    password = ""
    api_key = ""
    client = FirebaseAuthClient(api_key)
    res = client.sign_in_with_password(email, password)
    print(asdict(res))


if __name__ == "__main__":
    main()

from dataclasses import dataclass
from typing import TypedDict

import requests


class SignInWithPasswordRequest(TypedDict):
    email: str
    password: str
    returnSecureToken: bool


@dataclass
class SignInWithPasswordResponse:
    idToken: str
    email: str
    refreshToken: str
    expiresIn: str
    localId: str
    registered: bool


@dataclass
class FirebaseAuthClient:
    api_key: str

    def url(self, endpoint: str) -> str:
        return "https://identitytoolkit.googleapis.com/v1/{}?key={}".format(
            endpoint,
            self.api_key,
        )

    def sign_in_with_password(
        self,
        email: str,
        password: str,
        return_secure_token: bool = False,
    ) -> SignInWithPasswordResponse:
        payload = SignInWithPasswordRequest(email, password, return_secure_token)
        with requests.Session() as client:
            r = client.post(self.url("accounts:signInWithPassword"), data=payload)
            return SignInWithPasswordResponse(**r.json())

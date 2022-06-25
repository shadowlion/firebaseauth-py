from dataclasses import dataclass
from typing import TypedDict

import requests


class SignUpRequest(TypedDict):
    email: str
    password: str
    returnSecureToken: bool


@dataclass
class SignUpResponse:
    idToken: str
    email: str
    localId: str
    registered: bool
    displayName: str
    kind: str


class SignInWithPasswordRequest(TypedDict):
    email: str
    password: str
    returnSecureToken: bool


@dataclass
class SignInWithPasswordResponse:
    idToken: str
    email: str
    localId: str
    registered: bool
    displayName: str
    kind: str


@dataclass
class FirebaseAuthClient:
    api_key: str

    def url(self, endpoint: str) -> str:
        return "https://identitytoolkit.googleapis.com/v1/{}?key={}".format(
            endpoint,
            self.api_key,
        )

    def sign_up(
        self,
        email: str,
        password: str,
        return_secure_token: bool = False,
    ) -> SignUpResponse:
        payload = SignUpRequest(
            email=email,
            password=password,
            returnSecureToken=return_secure_token,
        )
        with requests.Session() as client:
            r = client.post(self.url("accounts:signUp"), data=payload)
            return SignUpResponse(**r.json())

    def sign_in_with_password(
        self,
        email: str,
        password: str,
        return_secure_token: bool = False,
    ) -> SignInWithPasswordResponse:
        payload = SignInWithPasswordRequest(
            email=email,
            password=password,
            returnSecureToken=return_secure_token,
        )
        with requests.Session() as client:
            r = client.post(self.url("accounts:signInWithPassword"), data=payload)
            return SignInWithPasswordResponse(**r.json())

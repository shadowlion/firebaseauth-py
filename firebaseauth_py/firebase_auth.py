from dataclasses import dataclass
from typing import Any, TypedDict, Union

import requests

from .errors import FirebaseErrorResponse


class SignUpRequest(TypedDict):
    email: str
    password: str
    returnSecureToken: bool


@dataclass
class SignUpResponse:
    idToken: str
    email: str
    refreshToken: str
    expiresIn: str
    localId: str
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


class FetchProvidersForEmailRequest(TypedDict):
    identifier: str
    continueUri: str


@dataclass
class FetchProvidersForEmailResponse:
    kind: str
    registered: bool
    sessionId: str


class DeleteAccountRequest(TypedDict):
    idToken: str


@dataclass
class FirebaseAuthClient:
    api_key: str

    def url(self, endpoint: str) -> str:
        return "https://identitytoolkit.googleapis.com/v1/{}?key={}".format(
            endpoint,
            self.api_key,
        )

    def __post_request(self, url: str, data: Any = None):
        with requests.Session() as client:
            return client.post(url, data=data)

    def sign_up(
        self,
        email: str,
        password: str,
        return_secure_token: bool = False,
    ) -> Union[SignUpResponse, FirebaseErrorResponse]:
        payload = SignUpRequest(
            email=email,
            password=password,
            returnSecureToken=return_secure_token,
        )
        r = self.__post_request(url=self.url("accounts:signUp"), data=payload)
        if "error" in r.json().keys():
            return FirebaseErrorResponse(**r.json())
        return SignUpResponse(**r.json())

    def sign_in_with_password(
        self,
        email: str,
        password: str,
        return_secure_token: bool = False,
    ) -> Union[SignInWithPasswordResponse, FirebaseErrorResponse]:
        payload = SignInWithPasswordRequest(
            email=email,
            password=password,
            returnSecureToken=return_secure_token,
        )
        r = self.__post_request(
            url=self.url("accounts:signInWithPassword"),
            data=payload,
        )
        if "error" in r.json().keys():
            return FirebaseErrorResponse(**r.json())
        return SignInWithPasswordResponse(**r.json())

    def fetch_providers_for_email(
        self,
        identifier: str,
        continue_uri: str,
    ) -> Union[FetchProvidersForEmailResponse, FirebaseErrorResponse]:
        payload = FetchProvidersForEmailRequest(
            identifier=identifier,
            continueUri=continue_uri,
        )
        r = self.__post_request(url=self.url("accounts:createAuthUri"), data=payload)
        if "error" in r.json().keys():
            return FirebaseErrorResponse(**r.json())
        return FetchProvidersForEmailResponse(**r.json())

    def delete_account(self, id_token: str) -> Union[None, FirebaseErrorResponse]:
        payload = DeleteAccountRequest(idToken=id_token)
        r = self.__post_request(self.url("accounts:delete"), data=payload)

        if "error" in r.json().keys():
            return FirebaseErrorResponse(**r.json())

        if r.status_code != 200:
            # TODO: raise Reponse Error of sorts
            pass

        return

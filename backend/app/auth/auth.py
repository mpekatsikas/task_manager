from fastapi import Security
from fastapi.security.api_key import APIKeyHeader
from starlette.authentication import AuthenticationError

class BasicAuthBackend:

    SCHEME = 'X-API-KEY'
    AUTH = APIKeyHeader(name=SCHEME)

    async def __call__(self, auth_token: str = Security(AUTH)) -> None:
        """
        Basic token authorization.

        :param auth_token: str, required
        :return: None
        """
        if auth_token != self._get_api_key():
            raise AuthenticationError('Unauthorized')

    @staticmethod
    def _get_api_key() -> str:
        """
        Determine the API key based on the environment.

        :return: str
            The API key value
        """
        return 'test_token'


auth = BasicAuthBackend()

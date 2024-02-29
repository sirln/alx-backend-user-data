#!/usr/bin/env python3
'''
Basic Authentication Module
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    Basic Authentication Class
    Inheriting from Auth Class to implement
    basic authentication.
    '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''
        Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Parameters:
        -----------
        authorization_header : str
            The Authorization header string.

        Returns:
        --------
        str or None:
            The Base64 part of the Authorization header if found,
            otherwise None.

        Notes:
        ------
        - Returns None if authorization_header is None.
        - Returns None if authorization_header is not a string.
        - Returns None if authorization_header doesn’t start
          by Basic (with a space at the end).
        - Otherwise, returns the value after Basic (after the space).
        '''
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[-1]

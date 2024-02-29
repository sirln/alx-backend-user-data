#!/usr/bin/env python3
'''
Basic Authentication Module
'''
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decode the Base64 string of the Authorization header
        for Basic Authentication.

        Parameters:
        -----------
        base64_authorization_header : str
            The Base64 string extracted from the Authorization header.

        Returns:
        --------
        str or None:
            The decoded value as UTF-8 string if the Base64 string
            is valid, otherwise None.

        Notes:
        ------
        - Returns None if base64_authorization_header is None.
        - Returns None if base64_authorization_header is not a string.
        - Returns None if base64_authorization_header is not a valid
          Base64 string.
        - Otherwise, returns the decoded value as UTF-8 string.
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password
        from the Base64 decoded value.

        Parameters:
        -----------
        decoded_base64_authorization_header : str
            The Base64 decoded value.

        Returns:
        --------
        (str, str) or (None, None):
            The user email and password if found, otherwise (None, None).

        Notes:
        ------
        - Returns (None, None) if decoded_base64_authorization_header is None.
        - Returns (None, None) if decoded_base64_authorization_header
          is not a string.
        - Returns (None, None) if decoded_base64_authorization_header
          doesn’t contain ':'.
        - Otherwise, returns the user email and password separated by ':'.
        """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = \
            decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password

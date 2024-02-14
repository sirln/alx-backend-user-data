'''
API authentication Module
'''

from flask import request
from typing import List, TypeVar

class Auth:

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        '''
        Return:
            - False
        '''
        if path is None or exclude_paths is None or len(exclude_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in exclude_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        '''
        Return:
            - None
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Return:
            - None
        '''
        return None

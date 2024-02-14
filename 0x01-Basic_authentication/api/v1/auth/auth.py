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
        return False

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

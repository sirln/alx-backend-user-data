'''
API authentication Module
'''

from flask import request


class Auth:

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        '''
        Return:
            - False -  path and excluded_paths
        '''

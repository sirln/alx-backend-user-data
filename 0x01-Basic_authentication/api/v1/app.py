#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None


auth_type = os.getenv("AUTH_TYPE")

if auth_type:
    if auth_type == "auth":
        auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def unauthorized(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """ Perform authenticaton and authorization
    checks before each request.

    Authentication and Authorization Workflow:
    1. If the 'auth' object is None, no authentication
       mechanism is configured, and the function
       returns without performing any checks.
    2. If the requested path is not in the list of paths
       that do not require authentication, the function
       proceeds with authentication checks.
    3. The 'require_auth' method of the 'auth' object
       is used to check if authentication is required
       for the request. If it returns False, indicating
       that authentication is not required, the function
       skips authentication checks for this request.
    4. The 'authorization_header' method of the 'auth'
       object is used to check if the authorization header
       is present in the request. If it returns None,
       indicating that the authorization header is missing,
       the function aborts the request with a 401
       Unauthorized status code.
    5. The 'current_user' method of the 'auth' object
       is used to check if the current user is authenticated.
       If it returns None, indicating that no user
       is authenticated, the function aborts the request
       with a 403 Forbidden status code.
    """
    exclude_paths = [
                        '/api/v1/status/',
                        '/api/v1/unauthorized/',
                        '/api/v1/forbidden/'
                    ]
    if auth is None:
        return
    path = request.path
    if not auth.require_auth(path, exclude_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

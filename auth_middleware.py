class AuthMiddleware():
    """
    Middleware for authenticating requests sent to a flask app
    """

    def __init__(self, app):
        self.app = app
        self.token = 'YHON36336hhngEYEY'

    def __call__(self, environ, start_response):
        # Validate token
        if self._authenticated(environ.get('HTTP_AUTHORIZATION')):
            return self.app(environ, start_response)
        return self._login(environ, start_response)

    def _authenticated(self, header):
        """
        Function to extract and validate user token from request header

        argument:
            header: request header

        output: 
            boolean: if user is validated this is set to true, otherwise false
        """

        try:
            if not header:
                return False

            _, token = header.split(None, 1)
            print("User has been validated? {}".format(token == self.token))

            return token == self.token
        except Exception:
            return False

    def _login(self, environ, start_response):
        start_response(
            '401 Authentication Required',
            [('Content-Type', 'text/html'), ('WWW-Authenticate', 'Bearer realm="mlflow server"')])
        return [b'Authentication Failed! Please check your authorization token or contact system admins.']

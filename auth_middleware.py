class AuthMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('----------------------------')
        print('Middleware function called')
        print('----------------------------')

        return self.app(environ, start_response)
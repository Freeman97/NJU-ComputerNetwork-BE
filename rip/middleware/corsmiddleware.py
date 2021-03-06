from django import http

class cors_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS,PATCH'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
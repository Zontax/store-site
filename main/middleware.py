from django.http import HttpResponse


class LogerMiddleware():
    
    def __init__(self, get_responce):
        self._get_responce = get_responce
    
    def __call__(self, request: HttpResponse):
        # print(f'REQUEST: {request.user}')    
        response = self._get_responce(request)
        #
        return response

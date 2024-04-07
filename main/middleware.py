from django.http import HttpResponse

from termcolor import cprint


class LogerMiddleware():
    
    def __init__(self, get_responce):
        self._get_responce = get_responce
    
    def __call__(self, request: HttpResponse):
        cprint(f'{request.user}', 'green', 'on_black')
        response = self._get_responce(request)
        
        return response

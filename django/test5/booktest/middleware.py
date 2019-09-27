from django.http import HttpResponse

class BlockIPSMiddleware(object):
    EXCLUDE_IPS = []
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')





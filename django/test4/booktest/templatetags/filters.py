# 自定义过滤器
# 过滤器其实就是python的函数
from django.template import Library

# 创建一个Libary类的对象
register = Library()


# 自定义过滤器至少有一个参数，最多只能有2个参数
@register.filter
def mod(num):
    '''判断num是否为偶数'''
    return num%2==0
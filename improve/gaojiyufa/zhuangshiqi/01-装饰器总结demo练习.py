def set_call_1(func):
    def call_func(*args, **kwargs):
        return "<h1>" + func() + "</h1>"
    return call_func

def set_call_2(func):
    def call_func(*args, **kwargs):
        return "<td>" + func() + "</td>"
    return call_func

@set_call_2
@set_call_1
def get_str():
    return "haha"

print(get_str())
def demo(*args,**kwargs):
    print(args)
    print(kwargs)


#  元组变量/字典变量
gl_nums = (1,2,3)
gl_xiaoming = {"name":"xiaoming"}
# demo(gl_nums,gl_xiaoming)
demo(*gl_nums,**gl_xiaoming)


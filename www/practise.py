girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
#字典推导
squrts = { i:'{}的平方是{}'.format(i,i**2) for i in range(10)}
print(squrts[8])
def square(x):
    '这是测试平方函数的注释'
    return x*x
print(square.__doc__)
def print_params_4(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
print_params_4(1,2,3,4,5,6,7,foo=1,bar=2)
num1 = (1,2,3)
num2 = (4,5,6)

for n1,n2 in zip(num1,num2):
    print(n1,":",n2);;;;;;



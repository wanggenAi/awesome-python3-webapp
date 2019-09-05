class ModeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, tuple):
                mappings[k] = v

        # 删除原来类中的属性
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModeMetaclass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        # 清洗整理插入的数据values
        args_temp = []
        for v in args:
            if isinstance(v, int):
                v = str(v)
            elif isinstance(v, str):
                v = """'%s'""" % v
            args_temp.append(v)
        sql = 'insert into %s (%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL 是 %s' % sql)


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')


class Classes(Model):
    cid = ('classid', 'int unsigned')
    name = ('classname', 'varchar(30)')
    email = ('cemail', 'varchar(30)')
    password = ('password', 'varchar(30)')



user = User(uid=12345, name='张三', email='d5736208@qq.com', password='qeqw24141')
user.save()

cl = Classes(cid=415, name='一年级', email='de2q4@qq.com', password='124125fawfaw')
cl.save()


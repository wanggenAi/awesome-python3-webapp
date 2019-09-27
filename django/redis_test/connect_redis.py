from redis import StrictRedis

if __name__ == '__main__':
    # 创建一个StrictRedis对象, 链接redis数据库
    try:
        sr = StrictRedis(host='192.168.208.4')
        # 添加一个key, 为name value qianqian
        res = sr.set('name', 'qianqian')
        print(res)
        result = sr.keys()
        print(result)
    except Exception as e:
        print(e)
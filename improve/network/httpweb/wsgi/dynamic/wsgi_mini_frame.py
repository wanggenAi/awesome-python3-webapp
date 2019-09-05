from pymysql import *
import re
import urllib.parse
import logging

URL_FUNC_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func()
        return call_func
    return set_func


@route(r'/index.html')
def index(ret):
    with open("./templates/index.html") as f:
        content =  f.read()
    # 创建connect连接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cs = conn.cursor()
    cs.execute('select * from info;')
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    html = ""
    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="%s">
            </td>
        </tr>
    """
    for line_info in stock_infos:
        html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4],
        line_info[5], line_info[6], line_info[7], line_info[1])
    content = re.sub(r"\{%content%\}", str(html), content)
    return content


@route(r'/center.html')
def center(ret):
    with open("./templates/center.html") as f:
        content = f.read()
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cs = conn.cursor()
    cs.execute('select i.code,i.short,i.chg,i.t'
               'urnover,i.price,i.highs,f.note_info from info as i '
               'inner join focus as f on i.id=f.info_id;')
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    html = ""
    tr_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                <a type="button" class="btn btn-default btn-xs" href="/show_update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvalue="%s">
            </td>
            </tr>
        """
    for line_info in stock_infos:
        html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4],
                               line_info[5], line_info[6], line_info[0], line_info[0])
    content = re.sub(r"\{%content%\}", str(html), content)
    return content

# URL_FUNC_DICT = {
#     "/index.py": index,
#     "/center.py": center
# }

@route(r'/add/(\d+)\.html')
def add_focus(ret):
    # 获取股票的代码
    stock_code = ret.group(1)
    # 判断是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = "select id from info where code = %s;"
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "抱歉没有（%s）这个股票" % stock_code
    # 判断是否关注过这个代码
    sql = """select i.id from info as i inner join focus as f where i.id = f.info_id and i.code = %s;"""
    cs.execute(sql, (stock_code,))
    if cs.fetchone():
        cs.close()
        conn.close()
        return "你已经关注(%s)过了，不能重复关注！" % stock_code
    # 关注这个股票，添加到关注表中
    sql = """insert into focus (info_id) select id from info where code = %s;"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()
    return "关注成功。。。"


@route(r'/del/(\d+)\.html')
def del_focus(ret):
    # 获取股票的代码
    stock_code = ret.group(1)
    # 判断是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = "select id from info where code = %s;"
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "抱歉没有（%s）这个股票" % stock_code
    # 判断是否关注过这个代码,关注过才可以删除
    sql = """select i.id from info as i inner join focus as f where i.id = f.info_id and i.code = %s;"""
    cs.execute(sql, (stock_code,))
    if cs.fetchone():
        sql = """delete from focus where info_id = (select id from info where code = %s);"""
        cs.execute(sql, (stock_code,))
        conn.commit()
        cs.close()
        conn.close()
        return "取消关注(%s)成功！！" % stock_code
    else:
        return "你没有关注过(%s)这个股票，不能取消关注" % stock_code


@route(r'/show_update/(\d+)\.html')
def show_update_page(ret):
    # 获取股票的代码
    stock_code = ret.group(1)
    # 判断是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = """select id from info where code = %s;"""
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "抱歉没有（%s）这个股票" % stock_code
    """显示修改的那个页面"""
    with open("./templates/update.html") as f:
        content = f.read()
    content = re.sub(r'\{%code%\}', stock_code, content)
    return content


@route(r'/update/(\d+)/(.*)\.html$')
def show_update_page(ret):
    # 获取股票的代码
    stock_code = ret.group(1)
    # 获取备注信息
    remmand = urllib.parse.unquote(ret.group(2))
    # 判断是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = """select id from info where code = %s;"""
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "抱歉没有（%s）这个股票" % stock_code
    """修改备注信息"""
    sql = """update focus set note_info = %s where info_id = (select id from info where code = %s);"""
    cs.execute(sql, (remmand, stock_code))
    conn.commit()
    cs.close()
    conn.close()
    return "更新成功！...."



def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    logging.basicConfig(level=logging.INFO,
                        filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info("访问的是，%s" % file_name)
    try:
        # func = URL_FUNC_DICT[file_name]
        # return URL_FUNC_DICT[file_name]()
        """
            {
                r'xxxxxx.html': index
            }
        """
        for url,func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            logging.warning('没有对应的函数。。')
            return "请求的url %s 并没有对应的函数.." % file_name
    except Exception as ret:
        return '产生了异常%s' % ret
    # if file_name == '/index.py':
    #     return index()
    # elif file_name == '/center.py':
    #     return center()
    # else:
    #     return 'Hello World大萨达达瓦大啊'

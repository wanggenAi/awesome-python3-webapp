import logging

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 创建一个handler，用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台上
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
# 定义日志输出的形式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logging.debug('这是 logger debug')
logging.info('这是 logger info')
logging.warning('这是 logger warning')
logging.error('这是 logger error')
logging.critical('这是 logger critical')

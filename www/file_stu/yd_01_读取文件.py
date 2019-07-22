# # 1.打开文件
# file = open("README")
#
#
# # 2.读取文件内容
# while True:
#     text = file.readline()
#     if not text:
#         break
#     print(text)
#
#
#
# #3.关闭文件
# file.close()
file_read = open("README")
file_write = open("README[复件]","w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()







import os
import multiprocessing

def copy_file(q,fname,old_folder,new_folder):
    """完成文件的复制"""
    # print("=====copy文件：从%s---->到%s 文件名是:%s" % (old_folder, new_folder, fname))
    old_f = open(old_folder+'/'+fname, "rb")
    fcontent = old_f.read()
    old_f.close()
    new_f = open(new_folder + '/' + fname, "wb")
    new_f.write(fcontent)
    new_f.close()

    # 如果拷贝完了文件，那么就向队列写入一个消息，表示已经完成
    q.put(fname)




def main():
    # 获取用户要copy的文件夹的名字
    old_folder = input("请输入要copy的文件夹的名字：")

    # 创建一个新的文件夹
    try:
        os.mkdir(old_folder + "[复件]")
    except:
        pass
    #  获取文件夹中所有的待copy的文件的名字 listdir()
    file_names = os.listdir("/data/"+old_folder)
    # 创建进程池
    po = multiprocessing.Pool(5)
    # 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 复制源文件夹中的文件到新文件夹中的文件去
    new_folder = old_folder + "[复件]"
    old_folder = "/data/"+old_folder
    for fname in file_names:
        po.apply_async(copy_file,(q,fname,old_folder,new_folder))

    po.close()
    #po.join()
    all_f_num = len(file_names)
    copy_ok_num = 0
    while True:
        fname = q.get()
        # print("已经完成copy: %s" % fname)
        copy_ok_num += 1
        print("\r拷贝的进度为 %.2f %%" % (copy_ok_num*100 / all_f_num),end="")
        if copy_ok_num == all_f_num:
            break
    print()


if __name__ == '__main__':
    main()
import os
import zipfile

startdir = '/home/lei/Documents/leetcode/flask'  # 要压缩的文件夹路径
zipname = '/home/lei/Documents/leetcode/flask/complete.zip'  # 压缩后文件夹的名字


def compress_zip(zipname, startdir):
    z = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        # print(fpath)
        fpath = fpath and fpath + os.sep or ''
        # print(fpath)
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath+filename)
    print ('压缩成功')
    z.close()

compress_zip(zipname, startdir)

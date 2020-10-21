import os
import zipfile

startdir = '/home/lei/qiming/cubex/app/store/workspace/A1/log' 
zipname = '/home/lei/qiming/cubex/app/store/workspace/log111.zip' 

# startdir = source_dir  # 要压缩的文件夹路径
# file_news = zipname  # 压缩后文件夹的名字

def compress_zip(zipname, startdir):
    z = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        print(fpath)
        fpath = fpath and fpath + os.sep or ''
        print(fpath)
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath+filename)
    print ('压缩成功')
    z.close()

compress_zip(zipname, startdir)

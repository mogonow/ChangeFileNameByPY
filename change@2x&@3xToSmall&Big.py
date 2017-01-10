import os;
import shutil



#去除文件夹中的@2x或者@3x
def rename(file):
    "Print usage message and terminate."
    filepath = file
    filelist = os.listdir(filepath)
    for files in filelist:
        Olddir = os.path.join(filepath,files)
        if os.path.isdir(Olddir):
            continue;
        filename = os.path.splitext(files)[0]
        filetype=os.path.splitext(files)[1]
        if filename.find("@3x")>=0:
            NewDir = os.path.join(filepath,filename.split("@3x")[0]+filetype)
            print("@3xResult=="+NewDir.title())
            if not os.path.isfile(NewDir):
                os.rename(Olddir,NewDir);
        if filename.find("@2x")>=0:
            smallNewDir = os.path.join(filepath,filename.split("@2x")[0]+filetype)
            print("@2xResult="+smallNewDir)
            if not os.path.isfile(smallNewDir):
                os.rename(Olddir,smallNewDir)

# 移动root中的@3x&@2x到大&小文件中
def move(file):

    filepath = file
    filelist = os.listdir(filepath)

    fileda= filepath + "/大"
    if not os.path.exists(fileda):
        os.makedirs(fileda)

    filexiao = filepath + "/小"
    if not os.path.exists(filexiao):
        os.makedirs(filexiao)
    for files in filelist:
        Olddir = os.path.join(filepath,files)
        if os.path.isdir(Olddir):
            continue;
        filename = os.path.splitext(files)[0]
        filetype=os.path.splitext(files)[1]
        if filename.find("@3x")>=0:
            bigDesPath=  os.path.join(fileda, filename.split("@3x")[0]+filetype)
            if os.path.exists(bigDesPath):
                print(bigDesPath+'已经存在')
            else:
                shutil.copy(Olddir,fileda)
        if filename.find("@2x")>=0:
            smallDesPath = os.path.join(fileda, filename.split("@2x")[0]+filetype)
            if os.path.exists(smallDesPath):
                print(smallDesPath + '已经存在')
            else:
                shutil.copy(Olddir,filexiao)
        rename(fileda)
        rename(filexiao)


def _main():
    file = "/Users/ku6/Downloads/连上看看APP_切图_20170105/切图/更多"
    move(file)

if __name__ == "__main__":
        _main()

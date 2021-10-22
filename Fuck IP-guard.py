# -*-coding:utf-8 -*-
from ntpath import join
import re
import sys
import os


# 获取日志中的dat文件路径
def getDatFile(line):
    for i in line:
        str = i
        allPath = str.split(',')[5]
        catchType = re.compile(r'C:(.*?)dat')
        partPath = catchType.findall(allPath)
        if(len(partPath) > 0):
            datPath = "C:" + "".join(partPath) + "dat"
            # print(DatPath)
            with open("./dat.txt", 'a+') as f:
                f.write(datPath+"\n")



def getExeFile(line):
    for i in line:
        str = i
        allPath = str.split(',')[5]
        catchType = re.compile(r'C:(.*?)exe')
        partPath = catchType.findall(allPath)
        if(len(partPath) > 0):
            exePath = "C:" + "".join(partPath) + "exe"
            with open("./exe.txt", 'a+') as f:
                f.write(exePath+"\n")
                


def getDllFile(line):
    for i in line:
        str = i
        allPath = str.split(',')[5]
        catchType = re.compile(r'C:(.*?)dll')
        partPath = catchType.findall(allPath)
        if(len(partPath) > 0):
            dllPath = "C:" + "".join(partPath) + "dll"
            with open("./dll.txt", 'a+') as f:
                f.write(dllPath+"\n")
                


def getRegedit(line):
    for i in line:
        str = i
        allPath = str.split(',')[5]
        end = allPath + ","
        catchType = re.compile(r'HKEY_(.*?),')
        partPath = catchType.findall(end)
        if(len(partPath) > 0):
            regeditPath = "HKEY_" + "".join(partPath)
            with open("./regedit.txt", 'a+') as f:
                f.write(regeditPath+"\n")


def getSysFile(line):
    for i in line:
        str = i
        allPath = str.split(',')[5]
        end = allPath + ","
        catchType = re.compile(r'C:(.*?)sys')
        partPath = catchType.findall(end)
        if(len(partPath) > 0):
            sysPath = "C:" + "".join(partPath) + "sys"
            with open("./sys.txt", 'a+') as f:
                f.write(sysPath+"\n")


# 对dat文件内容去重排序
def delDatRepeat():
    with open("./dat.txt", 'r') as f1:
        for i in set(sorted(f1.readlines())):
            with open("./dat1.txt", 'a+') as f2:
                f2.write(i)
    results = os.popen('sort dat1.txt').readlines()
    with open("./dat1.txt", 'a') as f3:
        #分割线，将去重排序后的内容追加到分割线后面
        f3.write("====================================================================\n")
        for i in results:
            f3.write(i)
            print(i + "     发现木马创建的dat文件，已记录")


def delExeRepeat():
    with open("./exe.txt", 'r') as f1:
        for i in set(sorted(f1.readlines())):
            with open("./exe1.txt", 'a+') as f2:
                f2.write(i)
    results = os.popen('sort .\exe1.txt').readlines()
    with open("./exe1.txt", 'a') as f3:
        f3.write("====================================================================\n")
        for i in results:
            f3.write(i)
            print(i + "     发现木马创建的exe文件，已记录")


def delDllRepeat():
    with open("./dll.txt", 'r') as f1:
        for i in set(sorted(f1.readlines())):
            with open("./dll1.txt", 'a+') as f2:
                f2.write(i)
    results = os.popen('sort dll1.txt').readlines()
    with open("./dll1.txt", 'a') as f3:
        f3.write("====================================================================\n")
        for i in results:
            f3.write(i)
            print(i + "     发现木马创建的dll文件，已记录")


def delRegeditRepeat():
    with open("./regedit.txt", 'r') as f1:
        for i in set(sorted(f1.readlines())):
            with open("./regedit1.txt", 'a+') as f2:
                f2.write(i)
    results = os.popen("sort regedit1.txt").readlines()
    with open("./regedit1.txt", 'a') as f3:
        f3.write("====================================================================\n")
        for i in results:
            f3.write(i)
            print(i + "     发现木马创建的注册表，已记录")

def delSysRepeat():
    with open("./sys.txt", 'r') as f1:
        for i in set(f1.readlines()):
            with open("./sys1.txt", 'a+') as f2:
                f2.write(i)
    results = os.popen("sort sys1.txt").readlines()
    with open("./sys1.txt", 'a') as f3:
        f3.write("====================================================================\n")
        for i in results:
            f3.write(i)
            print(i + "     发现木马创建的sys文件，已记录")



def main():
    filePath = "D:\病毒样本\Fuck IP-guard.txt"
    line = open(filePath, "r").readlines()
    #getDatFile(line)
    #delDatRepeat()
    #getExeFile(line)
    #delExeRepeat()
    #getDllFile(line)
    #delDllRepeat()
    #getRegedit(line)
    #delRegeditRepeat()
    getSysFile(line)
    delSysRepeat()


if __name__ == "__main__":
    main()

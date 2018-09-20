#!/usr/bin/env python
#coding=utf-8
import shutil

def targz_dir():
    archive_name = "basebak"
    root_dir = "../base"
    shutil.make_archive(archive_name, 'gztar', root_dir)

def copy():
    shutil.copy("config.ini","1.txt")
    shutil.copytree("../base","basebak")

def rm():
    shutil.move("1.txt","basebak/")
    shutil.rmtree("basebak")

if __name__=="__main__":
    copy()
    rm()
    targz_dir()
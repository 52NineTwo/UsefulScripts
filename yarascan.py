#!/usr/bin/env python
#coding:utf-8
import os
import sys
import yara
import hashlib

def md5sum(filename):
    """calc the md5 of `filename` """
    f = open(filename, 'rb')
    m = hashlib.md5()
    while True:
        data = f.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

def getFiles(path, filelist=[]):
    """get all files from `path` """
    for _ in os.listdir(path):
        item = os.path.join(path, _)
        if os.path.isfile(item):
            filelist.append(item)
        if os.path.isdir(item):
            getFiles(item, filelist)
    return filelist


def getRules(dirpath):
    """compile yara rules"""
    filepath = {}
    for _ in getFiles(dirpath):
        filepath[md5sum(_)] = _
    yararules = yara.compile(filepaths=filepath)
    return yararules

def scan(rules, path):
    """match the file with yara rules"""
    for _ in getFiles(path):
        fp = open(_, "rb")
        matches = rules.match(data=fp.read())
        fp.close()
        if len(matches) > 0:
            print("[+] " + _ + "\t\t\t" + str(matches))

def main():
    rulepath = sys.argv[1]
    malpath = sys.argv[2]
    yrules = getRules(rulepath)
    scan(rules = yrules, path=malpath)


if __name__ == "__main__":
    try:
        main()
    except IndexError as err:
        print("\n\tUsage:\n\t\tpython "+sys.argv[0]+" yara_rule_path  malware_path\n")

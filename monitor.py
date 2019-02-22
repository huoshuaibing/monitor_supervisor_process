#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import requests
import json
import subprocess
def send2dingtalk(**x):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a9ac2379c2eb09ef75d4108ccc8ee119ce59d3d364f350d68d679ccc2cb8cdf7'
    HEADERS = {
        "Content-Type": "application/json; charset=utf-8"
    }
    d = {
        "msgtype": "text",
        "text":{
            "content": x
        },
        "at":{
            "atMobiles":[
                "17600147211",
                "13691281371"
            ],
            "isAtAll":"false"
        }
    }
    d = json.dumps(d)
    requests.post(url, data=d, headers=HEADERS)
def check():
    cmd = subprocess.Popen(['supervisorctl'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output,error = cmd.communicate()
    output = output.split('\n')
    output =  output[:-2]
    target = []
    for i in output:
        if 'RUNNING' not in i:
            i = i.split() 
            target.append(i[0])
    if len(target) > 0:
        msg = {"服务器:test,以下队列已停止:":target}
        send2dingtalk(**msg)

if __name__ == "__main__":
    check()

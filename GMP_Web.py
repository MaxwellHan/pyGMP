# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:17:51 2018

@author: Aileen
"""

import flask
import pymysql
import json
from flask import request

app = flask.Flask(__name__)

@app.route("/")
def index():
    # return 'hello world'
    return flask.send_file("templates/index.html")

@app.route("/selectVideoList",methods=['POST'])
def selectVideoList():
    con = pymysql.connect(host='127.0.0.1', user="root", passwd="398597", db="gmp", port=3306, charset="utf8")
    cur = con.cursor()
    sql = "select * from videos"
    res = []
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for item in results:
            res.append({
                    'id':item[0],
                    'url':item[1],
                    'image_url':item[2],
                    'describe':item[3],
                    'title':item[4]
                   })
    except BaseException as e:
        print("query wrong!")
        print(e)

    return json.dumps(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0')


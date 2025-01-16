import logging
import allure
import requests
import pymysql

from config.config import *

@allure.step("2.发送 HTTP 请求")
def send_http_request(**request_data):
  res =  requests.request(**request_data)
  logging.info(f"2.发送HTTP请求响应文本为: {res.text}")
  return res


def send_jdbc_request(sql, index=0):
    conn = pymysql.Connect(
        host= DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        harset=DB_CHARSET
    )
    cur = conn.cursor()
            
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[index]
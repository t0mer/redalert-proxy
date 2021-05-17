#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, render_template, url_for, g, send_from_directory, jsonify, send_file
import urllib3
import os
from loguru import logger
import time
import json

os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['LANG'] = 'C.UTF-8'
REGION = os.getenv('REGION')
LANGUAGE = os.getenv("LANGUAGE")


logger.info("Monitoring alert for :" + REGION)


# Setting Request Headers
http = urllib3.PoolManager()
_headers = {'Referer': 'https://www.oref.org.il/',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36", 'X-Requested-With': 'XMLHttpRequest'}
alerts_url = 'https://www.oref.org.il/WarningMessages/alert/alerts.json'
history_url = 'https://www.oref.org.il/Shared/Ajax/GetAlarmsHistory.aspx?lang={}&mode=1'.format(
    LANGUAGE)
logger.info("alerts_url: " + alerts_url)
logger.info("history_url: " + history_url)


app = Flask(__name__)


@app.route('/alerts')
def alerts():
    r = http.request('GET', alerts_url, headers=_headers)
    r.encoding = 'utf-8'
    try:
        if r.data != b'':
            if REGION in r.data.decode('utf-8') or REGION == "*":
                return r.data
            else:
                return ''
        else:
            return ''
    except Exception as e:
        return jsonify(str(e))
    finally:
        r.release_conn()


@app.route('/history')
def history():
    data = '{"history": ""}'
    r = http.request('GET', history_url, headers=_headers)
    r.encoding = 'utf-8'
    try:
        history_json = json.loads(data)
        history_json["history"] = r.data.decode('utf-8')
        json_string = json.dumps(
            history_json, ensure_ascii=False).encode('utf8')
        return json_string.decode()
    except Exception as e:
        logger.error(str(e))
        return jsonify(data)
    finally:
        r.release_conn()


# Start Application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 03:32:21 2016

@author: Fabian Schvartzman
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld() :
    return "Hello World"

if __name__ == '__main__':
    app.debug=True
    app.run(host='www.stockpricepredict.com', port=80)
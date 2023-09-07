# inmport aplikasi flask untuk dipakai di web kita
import os

#import SQL utk akses database
from cs50 import SQL
# import flas untuk notifikasi pada web
# inmport jsonify utk formart data
# import redirect dan render_template untuk berpindah halaman web
# import request dan session untuk akses data
from flask import Flask, flas ,jsonify ,redirect, render_template, request, session

#mengatur nama aplikasi
app = Flask(__name__)

#mengatur URI(universal resource identifier), dan apa yang ditampilkan jika URI diakses
@app.route('/') #ketika http://127.0.0.1:5000 dipanggil, maka server akan mengeksekusi fungsi hello()
def hello(): #function dengan nama hello
    return 'hello, world'

#mengatur URI ke 
@app.route('/login')
def login():
    return 'halaman login'
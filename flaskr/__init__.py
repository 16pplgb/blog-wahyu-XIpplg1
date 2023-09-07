# inmport aplikasi flask untuk dipakai di web kita
from flask import Flask

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
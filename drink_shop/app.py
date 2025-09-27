from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pesan = None
    if request.method == 'POST':
        nama = request.form['nama']
        minuman = request.form['minuman']
        pesan = f"Terima kasih, {nama}! Pesanan {minuman} sedang diproses."

    daftar_minuman = [
        {"nama": "Es Teh", "harga": 5000, "gambar": "https://i.imgur.com/YwYy0cH.png"},
        {"nama": "Kopi Susu", "harga": 12000, "gambar": "https://i.imgur.com/mw03Ggc.png"},
        {"nama": "Jus Jeruk", "harga": 10000, "gambar": "https://i.imgur.com/KoZ9rBS.png"},
    ]

    return render_template("index.html", daftar_minuman=daftar_minuman, pesan=pesan)

if __name__ == '__main__':
    app.run(debug=True)

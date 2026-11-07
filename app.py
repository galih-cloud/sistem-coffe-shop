from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

# Data dummy menu kopi & barista
MENU_KOPI = {
    1: {"nama": "Caramel Macchiato", "harga": 28000, "kategori": "Coffee"},
    2: {"nama": "Manual Brew V60", "harga": 22000, "kategori": "Coffee"},
    3: {"nama": "Green Tea Latte", "harga": 25000, "kategori": "Non-Coffee"},
    4: {"nama": "Croissant Butter", "harga": 18000, "kategori": "Pastry"},
}
BARISTA_TERDAFTAR = ["eliazar", "nopal", "amsal"]


# --- 1. EMPAT ROUTE STATIS ---
@app.route("/")
@app.route("/beranda")
def beranda():
  return render_template("beranda.html")


@app.route("/tentang")
def tentang():
  return render_template("tentang.html")


@app.route("/produk")
def produk():
  return render_template("produk.html", menu=MENU_KOPI)


@app.route("/kontak")
def kontak():
  return render_template("kontak.html")


# --- 2. DYNAMIC ROUTE & VALIDASI ---
@app.route("/cek/<username>")
def cek_username(username):
  username = username.lower()
  if len(username) < 4:
    return "Error: Nama barista/staff minimal 4 karakter!", 400
  status = (
      "terdaftar sebagai Staff/Barista aktif"
      if username in BARISTA_TERDAFTAR
      else "tidak ditemukan dalam sistem"
  )
  return render_template("cek.html", username=username, status=status)


@app.route("/user/<username>")
def profil_user(username):
  return render_template("user.html", username=username)


# --- 3. ROUTE DENGAN CONVERTER INT & ABORT(404) ---
@app.route("/produk/<int:id>")
def detail_produk(id):
  p = MENU_KOPI.get(id)
  if p is None:
    abort(404)
  return render_template("detail_produk.html", produk=p, id=id)


# --- 4. PENGGUNAAN REDIRECT & URL_FOR ---
@app.route("/menu-lama")
def menu_lama():
  return redirect(url_for("produk"))


# --- 5. CUSTOM HALAMAN ERROR 404 ---
@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
  return render_template("404.html"), 404


if __name__ == "__main__":
  app.run(debug=True)
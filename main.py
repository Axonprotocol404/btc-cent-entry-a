import json, os, glob

def main():
    """Damped momentum BTC forecast untuk kompetisi btc-cent-forecast-01.

    Baca tiap case (*.in), ambil deret harga (nilai null/None dibuang),
    lalu prediksi: harga terakhir + 0.3 * momentum 480 menit (damped).
    Fallback: kalau riwayat < 480 poin, pakai momentum 60 menit terakhir
    (rata-rata 60 harga terakhir) -- lebih stabil daripada naive last-price
    karena tetap memakai informasi tren jangka pendek.
    """
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    inp = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    os.makedirs(out, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(inp, "*.in"))):
        case = json.load(open(f))
        pr = case["markets"][0]["prices"]
        # buang harga null/None agar tidak crash atau menghasilkan 'nan'
        pr = [p for p in pr if p is not None]
        cid = case["case"]
        if len(pr) >= 480:
            guess = pr[-1] + 0.3 * (pr[-1] - pr[-480])
        elif len(pr) >= 60:
            # fallback: rata-rata 60 menit terakhir (lebih stabil dari naive)
            guess = sum(pr[-60:]) / 60.0
        else:
            guess = pr[-1]  # riwayat sangat pendek: naive last-price
        with open(os.path.join(out, cid + ".out"), "w") as fh:
            fh.write("%.2f\n" % guess)

main()

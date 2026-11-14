import json, os, glob

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    inp = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    os.makedirs(out, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(inp, "*.in"))):
        case = json.load(open(f))
        pr = case["markets"][0]["prices"]
        cid = case["case"]
        guess = pr[-1] + 0.3 * (pr[-1] - pr[-480]) if len(pr) >= 480 else pr[-1]
        # damped 8h momentum; fallback naive when history is short
        with open(os.path.join(out, cid + ".out"), "w") as fh:
            fh.write("%.2f\n" % guess)

main()

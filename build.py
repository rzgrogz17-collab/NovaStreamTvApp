import json, glob

def birlestir(klasor, cikti):
    toplam = []
    for f in sorted(glob.glob(f"{klasor}/*.json")):
        with open(f, encoding="utf-8") as fh:
            toplam += json.load(fh)
    with open(cikti, "w", encoding="utf-8") as out:
        json.dump(toplam, out, ensure_ascii=False, separators=(",", ":"))
    print(f"{cikti}: {len(toplam)} kayit birlestirildi")

# Radyolar
birlestir("src", "stations.json")
# TV kanallari
birlestir("channels_src", "channels_fixed.json")

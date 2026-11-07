"""index.html'i src/app.html + Leaflet + harita verisi + plan'dan tek dosya olarak üretir.
Kullanım: python3 tools/build.py"""
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
rd = lambda p: (R / p).read_text(encoding="utf-8")
js = re.sub(r"//# sourceMappingURL=\S+", "", rd("vendor/leaflet/leaflet.js"))
out = (rd("src/app.html")
       .replace("/*@LEAFLET_CSS@*/", rd("vendor/leaflet/leaflet.css"))
       .replace("/*@LEAFLET_JS@*/", js + "\n")
       .replace("/*@GEO@*/", rd("data/geo_ankara.js") + "\n")
       .replace("<!--@PLAN@-->", rd("src/plan.html")))
assert "@*/" not in out and "<!--@" not in out
(R / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out.encode()), "bytes")

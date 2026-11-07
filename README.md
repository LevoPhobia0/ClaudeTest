# KortBul Ankara 🎾

Ankara'daki tenis kortlarını harita üzerinde gösteren uygulama fikrinin **planı ve tıklanabilir demosu**.

`index.html` tek dosyadır ve **hiçbir dış kaynak yüklemez**. Bu yüzden telefonda ve Claude uygulamasının içinde de çalışır.

- **🗺️ Harita:** 22 tesislik çekirdek liste var. Filtreler: açık, kapalı, karma ve ücret türü. Ayrıca konum seçme (semt, haritaya dokunma ya da cihaz konumu), en yakın kort ve mesafe, Google Maps veya Apple Haritalar'da yol tarifi, yıldızlı yorumlar ve her tıklamada "Temiiiis!" sesi.
- **📋 Plan:** veri kaynakları araştırması, veri modeli, mimari, yol haritası ve riskler.

## Dosyalar
| Dosya | Ne işe yarar |
|---|---|
| `src/app.html` | Uygulama kodu (şablon) |
| `src/plan.html` | Plan sekmesinin içeriği |
| `data/geo_ankara.js` | Ankara ilçe sınırları (geoBoundaries), ana yollar ve yerleşim alanları (Natural Earth), sadeleştirilmiş |
| `vendor/leaflet/` | Leaflet 1.9.4 (BSD-2) |
| `tools/build.py` | Yukarıdakileri birleştirip `index.html` üretir: `python3 tools/build.py` |
| `tools/build_geo.py` | Ham GeoJSON'dan `data/geo_ankara.js` üretir |

> Not: Çekirdek listedeki kort konumları yaklaşıktır. Ücretlerin çoğu yayımlanmadığı için "bilinmiyor" olarak işaretlendi; Faz 0'da doğrulanacak.

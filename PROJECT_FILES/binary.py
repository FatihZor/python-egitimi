def binary_dosya_okuma_islemi(dosya_yolu):
    with open(dosya_yolu, "rb") as dosya:
        icerik = dosya.read()
        return icerik.decode(encoding='utf-8')

dosyam = "data\\sayilar.txt"
sonuc = binary_dosya_okuma_islemi(dosyam)
print(sonuc)
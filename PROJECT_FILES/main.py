import datetime

def dosya_okuma_islemi(dosya_path: str, satir_satir: bool = False) -> list or str or None:
    try:
        with open(dosya_path) as dosya:
            if satir_satir:
                return dosya.readlines()
            else:
                return dosya.read()
    except:
        return None

def dosya_yazma_islemi(dosya_path: str, yazilacak_metin: str) -> bool:
    if type(yazilacak_metin) is str:
        formatsiz_now = datetime.datetime.now()
        formatli_now = formatsiz_now.strftime("%H:%M:%S %d/%m/%Y")
        yazilacak_metin = str(formatli_now) + "\t" + yazilacak_metin + "\n"
    else:
        print("Hata: Yazılacak Metin String Değil!")
        return False
    
    try:
        with open(dosya_path, "a") as dosya:
            dosya.write(yazilacak_metin)
            return True
    except Exception as e:
        print("Hata: " + str(e))
        return False

okunacak_dosyam = "data\\sayilar.txt"
yazilacak_dosyam = "data\\sonuclar.txt"
dosya_icerigi = dosya_okuma_islemi(dosya_path=okunacak_dosyam, satir_satir=True)

sonuc = 0
for satir in dosya_icerigi:
    for karakter in satir:
        if karakter.isdigit():
            sonuc = sonuc + int(karakter)

print(sonuc)

if dosya_yazma_islemi(yazilacak_dosyam, str(sonuc)):
    print("Sonuçlar başarılı şekilde yazıldı!")
else:
    print("Sonuçlar başarılı şekilde yazılamadı!")
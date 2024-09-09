# Başlangıç liste tanımı
liste1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Öğrenci numarasının son 3 hanesini girin
ogrenci_numarasi_son_3_hane = input("Öğrenci numaranızın son 3 haneyi girin: ")

# Liste üzerinde dolaşarak 6000'den büyük ilk sayının ardına numarayı ekleyen fonksiyon
def numara_ekle(liste, numara):
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            numara_ekle(liste[i], numara)  # Alt listelerde de arama yap
        elif liste[i] > 6000:
            liste.insert(i, numara)  # Numarayı bulduğumuz yerin hemen önüne ekleyin
            break

# Fonksiyonu kullanarak numarayı ekleme
numara_ekle(liste1, ogrenci_numarasi_son_3_hane)

# Yeni listeyi gösterme
print("Güncellenmiş liste:", liste1)
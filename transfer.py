print("="*30)

print("Fatih Karagümrük Transfer Paneli;")

print("="*30)
playerlist = ["Cisse","Sannata","İ.Çipe","Güven","Berat","Şener"]
print("Gündemdeki Transferler = ",playerlist)
select = input("Hangi oyunyunun bilgilerini almak istiyorsunuz ?")
print("="*30)

loading = "Bilgiler yükleniyor..."
print(loading)
if select == "Cisse":
  name = "Pappis Cisse"
  fromm = "Nigeria"
  age = "36"
  performance = "Match = 458, Gol = 217, Asists = 34"
  foot = "Sğ"
  position = "Forvet"
  print("=" * 30)
  print("İsim = ",name)
  print("Ülke = ",fromm)
  print("Yaş = ",age)
  print("Performans = ",performance)
  print("Ayak = ",foot)
  print("Pozisyon = ",position)
  print("=" * 30)
elif select == "Samatta":
  name = "Mbawna Samatta"
  fromm = "Tanzania"
  age = "29"
  performance = "Match = 282, Gol = 130, Asists = 25"
  foot = "Sğ"
  position = "Forvet"
  print("=" * 30)
  print("İsim = ", name)
  print("Ülke = ", fromm)
  print("Yaş = ", age)
  print("Performans = ", performance)
  print("Ayak = ", foot)
  print("Pozisyon = ", position)
  print("=" * 30)
elif select == "Berat":
  name = "Berat"
  fromm = "Türkey"
  age = "24"
  performance = "Match = 162, Gol = 15, Asists = 24"
  foot = "Sğ"
  position = "Merkez Orta Saha"
  print("=" * 30)
  print("İsim = ", name)
  print("Ülke = ", fromm)
  print("Yaş = ", age)
  print("Performans = ", performance)
  print("Ayak = ", foot)
  print("Pozisyon = ", position)
  print("=" * 30)
elif select == "İ.Çipe":
  name = "İsmail Çipe"
  fromm = "Turkey"
  age = "32"
  performance = "Match = 350 Toplam yenilen gol = 420"
  foot = "Sğ"
  position = "Kaleci"
  print("=" * 30)
  print("İsim = ", name)
  print("Ülke = ", fromm)
  print("Yaş = ", age)
  print("Performans = ", performance)
  print("Ayak = ", foot)
  print("Pozisyon = ", position)
  print("=" * 30)
elif select == "Güven":
  name = "Güven Yalçın"
  fromm = "Türkey"
  age = "23"
  performance = "Match = 120, Gol = 52, Asists = 14"
  foot = "Sğ"
  position = "Forvet"
  print("=" * 30)
  print("İsim = ", name)
  print("Ülke = ", fromm)
  print("Yaş = ", age)
  print("Performans = ", performance)
  print("Ayak = ", foot)
  print("Pozisyon = ", position)
  print("=" * 30)
elif select == "Şener":
  name = "Şener Özbayraklı"
  fromm = "Turkey"
  age = "33"
  performance = "Match = 395, Gol = 12, Asists = 44"
  foot = "Sğ"
  position = "Sağ bek"
  print("=" * 30)
  print("İsim = ", name)
  print("Ülke = ", fromm)
  print("Yaş = ", age)
  print("Performans = ", performance)
  print("Ayak = ", foot)
  print("Pozisyon = ", position)
  print("=" * 30)
else:
  print("Sistemde oyuncu bulunamadı"
        "")

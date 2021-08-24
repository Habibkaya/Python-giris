import random

print(random.randrange(1, 10))
#İmport modülü bize rastgele sayı yazdırır!

y = int(2.8)
print(type(y))                         # Dosya tipini yazdırır

a = "HHabib Kaya"
print(a[1])                            # A değişkenin içindeki 1 indexi yazdırır

for x in "abibKaya":                   # abibKayayı alt alta yazdırır
  print(x)

txt = "The best things in life are Free!"
print("free" in txt)                   # Eğer ki txt değikenin içinde free kelimesi varsa true döndürür

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")      # Txt değişkenine bakar ve içinde free kelimesi geçiyorsa
                                        # "Yes, 'free' is present" yazdırır Konsola

txt = "The best things in life are free!"
print("expensive" not in txt)           # Eğer ki "expensive" Kelimesi yoksa True döndürür

txt = "The best things in life are free!"
if "expensive" not in txt:              # 18,20.satırlardaki kodun tam tersi işlevini görür.
 print("No, 'expensive' is NOT present.")

b = "Hello, World!"                     # Karakterleri başlangıçtan 5 konumuna getirir
print(b[:5])

b = "Hello, World!"                     # Karakterleri 2. konumdan sonuna kadar alın:
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"                     #Hepsini büyük harfler ile yazar
print(a.upper())

a = "Hello, World!"
print(a.lower())                        #Hepsini küçük harfler ile yazar

a = "Hello, World!"
print(a.replace("H", "J"))              #Belirtiğimiz harf ile aynı şekilde belirtiğimiz harf yerine geçer.

a = "Hello, World!"
print(a.split(","))                     #['Hello', ' World!'] Olarak döndürür

a = "Hello"
b = "World"
c = a +" "+ b
print(c)                                #Arasında boşluk bırakarak yazdırır

#format() yöntemi sınırsız sayıda argüman alır ve ilgili yer tutuculara yerleştirilir:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = "Yeni gelen cocugun adı \"Habib Kaya\" idi "
print(txt)                               #Cümle içerisinde "" kullanmamız gerekirse aklımızda bulunsun :)

#nickName = input("İsiminizi girin")
#x = nickName.capitalize()
#print(nickName)

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

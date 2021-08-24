#Python Listeler:
#Liste değiştirilebilir, yani bir liste oluşturulduktan
#Sonra listedeki öğeleri değiştirebilir, ekleyebilir ve kaldırabiliriz.
#
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple","banana","lemon"]
print(len(thislist))                              #Listenin kaç öğeye sahip olduğunu belirtir

#Bir liste farklı veri türleri içerebilir:

mylist1 = ["apple", "banana", "cherry"]
mylist2 = [1, 5, 7, 9, 3]
mylist3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

print(type(list1))

thislist = list(("apple", "banana", "cherry"))   #Çift yuvarlak parantezlere dikkat edin
print(thislist)

"""
Liste => sıralı ve değiştirilebilir bir koleksiyondur. Yinelenen üyelere izin verir.
Tuple => sıralı ve değişmez bir koleksiyondur. Yinelenen üyelere izin verir.
Set => sırasız ve indekslenmemiş bir koleksiyondur. Çift üye yok.
Dictionary => sıralı* ve değiştirilebilir bir koleksiyondur. Çift üye yok.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])                             #İndex sırasına göre ekrana yazdırır

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])                            #Arama dizin 2 de dahil başlar ve dizin 5'te dahil değildir

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])                             #Bu örnek, öğeleri baştan sona döndürür, ancak kiwiden sonrası dahil değildir

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])                             #Bu örnekte cherryden sonrasına kadar yazdırır

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")   #Listede apple olup olmadığını kontrol eder

#Şimdi listemizdeki index değerlerini değiştirmeyi deneyelim.

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)                                  #Listede 1.index numarasındaki yani banana ile blackcurrant' değiştirir
#Birden fazla index değiştirelim şimdi
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)                                  #banana ile cherry değişir.
#Eklenen öğelerin sayısı değiştirilen öğelerin sayısıyla eşleşmediğinde listenin uzunluğu değişir

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)                                  #watermelon 2.indekse geçer

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)                                 #append değer eklemek için kullanılır listenin sonuna ekler

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)                                 #extend listeleri birleştirir

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)                                 #Aynı şekilde bir tuple ile listeyide birleştirebiliriz

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)                                 #"Remove" Listeden muzu kaldırdı

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)                                 #"pop" ise belirtilen indeks numarasındaki değeri kaldırır
                                                #Dizeyi belirtmez isek listedeki son öğeyi kaldırır

thislist = ["apple", "banana", "cherry"]
del thislist                                    #Tüm listeyi silmek istersek "del" kullanabiliriz

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)                                 #Liste elemanlarını tamamiyle siler

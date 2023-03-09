metin = "Furkan" #=> String veri tipleri metinsel ifadeleri içerir.
sayisal = 16 #=>int veri tipleri sayısal ifadeleri içerir.
sayi = 3.1 #=>Float veri tipi küsüratlı sayısal ifadeleri içerir.
#Bool veri tipi şartlı ifadeleri içerir. İfade şarta göre doğru ise True, eğer değilse False döndürür.
#list ve tuple veri tipi sıralanan ifadeleri içerir.

print("---------------------------------------------------")
#string => metinsel ifadeler
ziraatverileri = "Ziraat Verileri"
piyasa = "Piyasalar"
kredihesap = "Kredi Hesaplama"
basvuru = "Başvurular"
print(ziraatverileri) 
print(piyasa) 
print(kredihesap) 
print(basvuru)
print("---------------------------------------------------")
#integer => sayısal ifadeler
kreditutarı = 5000
vade = 60
#float, doubel, decimal => ondalık ifadeler
faizorani = 1,99

#bool, boolean => True veya False
yukseliste = True
dususte = False

#matematiksel operatorler
print(844526 * 216489)
print(844526 + 216489)
print(844526 - kreditutarı)
print(844526 / 216489)
print(kreditutarı + vade)
yenikreditutari = kreditutarı / vade
print(yenikreditutari)

#mod alma
print(250 % 3)
print(kreditutarı % vade)

#mantıksal operatorler
print(2 > 3)
print(5 > 3)
print(2 > 3 and 5 > 3)
print(2 > 3 or 5 > 3)
print(4 > 3 and 5 < 3 or 2 < 3)
print(1 != 2)
print(2 != 2)

#if else elif
sayi1 = 31
sayi2 = 36

if sayi1 > sayi2:
    print("Birinci sayı ikinci sayıdan büyüktür.")
elif sayi1 == sayi2:
    print("İki sayı birbirine eşittir.")
else:
    print("Birinci sayı ikinci sayıdan küçüktür.")
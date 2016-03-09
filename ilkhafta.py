Veri Türleri
Numeric, String, Boolean
Numeric = float, int, complex,
String = String
Boolean = True, False


a= 2
typa(a) --> Çıktı int
a=2+5j ,,, a="Merhaba" ,,, a=6.1 gibi 
typa(a) --> tipini döndürür.

Matematiksel İşlemler
5 / 2 --> Çıktı 2.5 //Bölme İşlemi
5 // 2 --> Çıktı 2 //Bölüm
5 % 2 --> Çıktı 1 // Kalan

Hem Bölüm hem kalan istersek 
divmod(5,2) --> Çıktı (2,1) 


Karmaşık Sayı İşlemleri
a = 2 + 3j
a.real -> Gerçek Kısmı Çıktı 2 
a.imag -> İmajinal Kısmı Çıktı 3
a.conjugate -> Eşleniği Kısmı (2+3j)

Dönüştürme Tipleri 
int(2.3) --> Çıktı 2
float(2) --> Çıktı 2.0
str(2) --> Çıktı '2'
abs(-2) --> Mutlak değer Çıktı 2
pow(2,3) -> 2 üssü 3 'den Çıktı 8
2**3 -> 2 üssü 3 işlemini yapar

round(2,5) Çıktı 2 ,, 2,6 olsaydı 3 olacaktı.
round(2,41571,2) Çıktı 2,41



import math --> math kütüphanesini ekle
math. yazıp Enterladığımızda bize kullanabileceğimiz fonksiyonları gösteriyor.

s="merhaba"
len(s) uzunluğu verir 7
s.capitalize() ilk harfi büyük yap
s.center(10) 10 karakterli haline getir ortala
s.center(10,"*") ortala boşluklara * koy
s.ljust(10,"*") 10 karakterli haline getir sola yasla yildiz koy



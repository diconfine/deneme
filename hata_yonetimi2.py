try:
    sayi1 = int(input("sayı 1 : "))
    sayi2 = int(input("sayi 2 : "))
    
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2
    mod = sayi1 % sayi2

    print(f" Sayıların Toplamı: {toplam}\n Sayıların Farkı : {fark}\n Sayıların Bölümü : {bolum} \n Sayıların Çarpımı : {carpim} \n Sayıların Modu : {mod}")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionEror")
except OverflowError:
    print("OverflowError")
except:
    print("Hata Yakalama Alanı")



# ctrl + k + c => seçili alanı yorum satırı yapar.
# ctrl + k + u => seçili alanı yorum satırından cıkarır.
# alt + shift + f => kodları düzenler.
# alt + z => woordwrap (ekran sonunda satırı alta alır)


# convert : elinizdeki değeri faklı değerlere (veri tiplerine) çevirmek için kullanılır.

# int()   : tam sayı veri tipine çevirir
# str()   : string (metinsel) veri tipine cevirir.
# floot() : ondalıklı sayı veri tipine cevirir.
# chr()   : verdiğiniz sayısal değerin, metinsel değerini tesli eder.
# ord()   : verdiğiniz karkterin, ascii (sayılsal) değerini teslim eder.


x = input("sayı 1 ")
y = input("sayı 2 ")

z = float(x) + float(y)
print(z)

print(chr(55), ord("d"))
print(chr(88), ord("k"))
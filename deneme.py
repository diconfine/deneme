firstname = "Serhat"
surname = "BAL"
age = 25
weight = 60.3

print(type(firstname))
print(type(age))
print(type(weight))

print(firstname,surname,age,weight, sep=" - ")

fullname = firstname + " " + surname
print(fullname)
print("Personel Adı: " + fullname)
print("Personel Adı:" ,fullname)
print((fullname + "\n" ) *5  )
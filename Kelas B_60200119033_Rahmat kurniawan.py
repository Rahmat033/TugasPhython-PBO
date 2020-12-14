class format :
    __vendor_message = "segitiga sama kaki"
    name     =""
    alas     =""
    tinggi   =""
    luas     =""

    def __init__(self,name):
        self.name = name

    def get_vendor_message(self):
        print(self.__vendor_message)

    def set_alas(self, alas):
        self.alas = alas

    def set_tinggi(self, tinggi):
        self.tinggi = tinggi

    def set_luas(self, luas):
        self.luas = luas

sg  = format("objek segitiga sama kaki pertama")
sg1 = format("objek segitiga sama kaki kedua")
sg2 = format("objek segitiga sama kaki ketiga")

sg.set_alas(25)
sg1.set_alas(27)
sg2.set_alas(29)

sg.set_tinggi(40)
sg1.set_tinggi(42)
sg2.set_tinggi(45)

sg.luas = sg.alas * sg.tinggi
sg1.luas = sg1.alas * sg1.tinggi
sg2.luas = sg2.alas * sg2.tinggi

print("%s\nAlas segitiga siku-siku pertama adalah : %d\nTinggi segitiga siku-siku pertama adalah : %d\nLuas segitiga siku-siku pertama adalah : %d\n"%
      (sg.name,sg.alas,sg.tinggi,sg.luas))
print("%s\nAlas segitiga siku-siku pertama adalah : %d\nTinggi segitiga siku-siku pertama adalah : %d\nLuas segitiga siku-siku pertama adalah : %d\n"%
     (sg1.name,sg1.alas,sg1.tinggi,sg1.luas))
print("%s\nAlas segitiga siku-siku pertama adalah : %d\nTinggi segitiga siku-siku pertama adalah : %d\nLuas segitiga siku-siku pertama adalah : %d\n"%
     (sg2.name,sg2.alas,sg2.tinggi,sg2.luas))

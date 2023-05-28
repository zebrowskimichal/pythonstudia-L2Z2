##Zmodyfikowalem klasy Human i Cat, poniewaz nie mialy weogole albo mialy zbyt malo elementow wspolnych, aby korzystac z dziedziczenia


class Animal:
    def __init__(self, imie, wiek, wzrost, waga):
        self.imie = imie
        self.wiek = int(wiek)
        self.konwertujWzrost(int(wzrost))
        self.konwertujWage(int(waga))

    def konwertujWzrost(self, wzrostWcm):
        wzrostWmm = wzrostWcm * 10
        self.wzrost = wzrostWmm
         
    def konwertujWage(self, wagaWg):
        wagaWkg = wagaWg / 1000
        self.waga = wagaWkg

    def wolaj(self):
        print("Hej, " + self.imie + "!")

    def jedz(self):
        pass


##Abstrakcja jest przydatna w sytuacji gdy potrzebujemy miec jedna glowna klase, w ktorej bedzie zawarte wiele metod, zmiennych. Klasy dziedziczace z tej glownej klasy, beda natomiast posiadac 'wlasne', abstrakcyjne metody, ktore tak naprawde ustala sie dopiero podczas operacji dziedziczenia

##Dziedziczenie z pewnoscia przyda sie w sytuacji, gdy mamy wiele takich samych zmiennych, metod w roznych klasach. Przydatne szczegolnie, aby zmniejszyc dlugosc naszego kodu.


class Object:
    def __init__(self, ilemm):
        self.ilemm = ilemm

    def rosnij(self, lista):
        for x in lista:
            Animal.wzrost = self.wzrost + self.ilemm

    def Przedstawianie(lista):
        for x in lista:
            Animal.wolaj()


class Human(Animal):
    def __init__(self, imie, wiek, wzrost, nazwisko, plec, waga):
        super().__init__(imie, wiek, wzrost, waga)
        self.nazwisko = nazwisko
        self.plec = plec

    def daneOsobowe(self):
        print("Imie: " + self.imie)
        print("Nazwisko: " + self.nazwisko)

    def daneGenetyczne(self):
        print("Plec: " + self.plec)
        print("wzrost: " + str(self.wzrost))

    def wszystkieInformacje(self):
        print("Imie: " + self.imie)
        print("Nazwisko: " + self.nazwisko)
        print("Plec: " + self.plec)
        print("wzrost: " + str(self.wzrost))
        print("wiek: " + str(self.wiek))

    def rosnij(self, nowyWzrost):
        self.wzrost = nowyWzrost

    def slub(self, noweNazwisko):
        self.nazwisko = noweNazwisko
        print("Gratulacje Pani " + noweNazwisko + "!")

    def wolaj(self):
        print("Hej! Jestem " + self.imie)

    def jedz(self):
        print("Czlowiek je mieso")

    def BMI(self):
        self.__ciezar = self.waga
        self.__bmi = self.__ciezar / self.wzrost ** 2
        if(self.__bmi < 18.5):
            print("niedowaga")
        if(self.__bmi >= 18.5 and self.__bmi < 25):
            print("waga prawidlowa")
        if(self.__bmi >= 25):
            print("nadwaga")

##Hermetyzacja przydaje sie w sytuacji gdy na zewnatrz klasy chcemy udostepnic tylko to co jest niezbedne. Ogranicza to tez opcje "popsucia" naszej klasy, np poprzez zmiane jakiejs zmiennej wewnatrz tej klasy

##czlowiek = Human("Anita", "Wlodarczyk", "Mezczyzna", 21, 180)
##czlowiek.daneOsobowe()
##czlowiek.daneGenetyczne()
##czlowiek.wszystkieInformacje()
##czlowiek.rosnij(190)
##czlowiek.daneGenetyczne()
##czlowiek.slub("Ciesla")
##czlowiek.daneOsobowe()
czlowiek = Human("Andrzej", 28, 180, "JSON", "m")
czlowiek.daneOsobowe()
czlowiek.wolaj()
czlowiek.jedz()
##############


class Cat(Animal):
    def __init__(self, imie, wiek, wzrost, rasa, waga):
        super().__init__(imie, wiek, wzrost, waga)
        self.rasa = rasa

    def Wolaj(self):
        print("Chodz, tu: " + self.imie)

    def daneKota(self):
        print("Imie: " + self.imie)
        print("Wiek: " + str(self.wiek))
        print("Rasa: " + self.rasa)
        print("Waga: " + str(self.waga))

    def noweImie(self, noweImie):
        self.imie = noweImie

    def zmienWage(self, nowaWaga):
        self.waga = nowaWaga
        print("Kot zmienia wage, na: " + str(self.waga) + " kg")

    def wolaj(self, imie):
        print("Meow! Meow, meow " + self.imie)

    def jedz(self):
        print("Kot je rybki")


# kot = Cat("Andrzej", 2010, "Dachowiec", 16500)
# kot.Wolaj()
# kot.wiek()
# kot.daneKota()
# kot.noweImie("Andruch")
# kot.Wolaj
# kot.zmienWage(10200)

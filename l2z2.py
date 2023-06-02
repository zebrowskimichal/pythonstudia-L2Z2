##Zmodyfikowalem klasy Human i Cat, poniewaz nie mialy wogole albo mialy zbyt malo elementow wspolnych, aby korzystac z dziedziczenia (na potrzeby tego zadania)

##Klasa nadrzedna
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


##Abstrakcja jest przydatna w sytuacji gdy potrzebujemy miec jedna glowna klase (chcemy zdefiniowac ogolna strukture klasy), w ktorej bedzie zawarte wiele metod. Klasy dziedziczace z tej glownej klasy, beda natomiast posiadac 'wlasne', abstrakcyjne implementacje tychze metod, ktore tak naprawde ustala sie dopiero podczas operacji dziedziczenia

##Dziedziczenie z pewnoscia przyda sie w sytuacji, gdy mamy wiele takich samych zmiennych, metod w roznych klasach. Przydatne szczegolnie, aby zmniejszyc dlugosc naszego kodu i poprawic ogolna spojnosc. Z wad nalezy wymienic mozliwosc tworzenia bardzo wielu dziedziczen, co na koncu moze mocno utrudnic zrozumienie kodu, jego testowanie oraz debugowanie

##Dodatkowa klasa dziedziczaca z klasy Animal
class Object(Animal):
    def __init__(self, imie, wiek, wzrost, waga, rodzaj):
        super().__init__(imie, wiek, wzrost, waga)
        self.rodzaj = rodzaj

    def wolaj(self):
        print("Halo, jestem " + self.imie + "!")
        print("Jestem " + self.rodzaj)

#################
obiekt1 = Object("Jaskolek", 1, 20, 2, "ptak")
obiekt1.wolaj()
obiekt2 = Animal("Andrzej", 6, 15, 15)
obiekt2.wolaj()
print("#############################################################")
#################

#Polimorfizm pozwala na zdefiniowanie wielu wersji tej samej metody w roznych klasach, ktore dziedzicza z jednej klasy. Pozwala, to na dostosowanie metody do swoich potrzeb (potrzeb klasy podrzednej). Do wad nalezy zaliczyc trudnosc w zrozumieniu kodu, przy zbyt duzym wykorzystaniu polimorfizmu oraz mozliwa utrata wydajnosci

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

##Hermetyzacja przydaje sie w sytuacji gdy na zewnatrz klasy chcemy udostepnic tylko to co jest niezbedne. Ogranicza to tez opcje "popsucia" naszej klasy (np poprzez zmiane jakiejs zmiennej wewnatrz tej klasy). Z wad nalezy jednak wymienic mozliwosc niekontrolowanego dostepu i zmiany, przez brak 'surowej' kontroli dostepu- w pythonie podkreslenie ('_') jest tylko 'znakiem' dla programisty, programista nie musi wcale przesatrzegac tej konwencji

#################
czlowiek = Human("Anita", 21, 180, "Wlodarczyk", "Kobieta", 53)
czlowiek.daneOsobowe()
czlowiek.daneGenetyczne()
czlowiek.wszystkieInformacje()
czlowiek.rosnij(190)
czlowiek.daneGenetyczne()
czlowiek.slub("Ciesla")
czlowiek.wolaj()
czlowiek.jedz()
czlowiek.BMI()
print("#############################################################")
#################


class Cat(Animal):
    def __init__(self, imie, wiek, wzrost, rasa, waga):
        super().__init__(imie, wiek, wzrost, waga)
        self.rasa = rasa

    def wolaj_chodz(self):
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

#################
kot = Cat("Andrew", 8, 15, "Dachowiec", 14)
kot.wolaj_chodz()
kot.daneKota()
kot.noweImie("Andruch")
kot.wolaj
kot.zmienWage(5)
print("#############################################################")
#################
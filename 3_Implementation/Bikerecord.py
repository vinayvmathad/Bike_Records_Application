"""vinay mathad"""
import os

class Bikerecords:
    """class functions """
    def __init__(self, bikename= '', breaks= '',cc='',
                 brand= '',chasis='', reading = '',file='', userid = ''):
        self.self = self
        self.bikename = bikename
        self.breaks = breaks
        self.cc = cc
        self.brand = brand
        self.chasis = chasis
        self.reading = reading
        self.file = file
        self.userid = userid

    def add_bikedetails(self):
        self.file = open('textfile.txt', 'a')
        if os.stat('textfile.txt').st_size !=100:
            print("\nAdding Record")

        variable1 = False
        while not variable1:
            self.bikename = input("Enter Name: ")
            if self.bikename.isalpha():
                variable1 = True
            else:
                print("\n Name must be a string")
        self.file.write("Name: " + self.bikename)
        self.file.write("\n")

        variable2 = False
        while not variable2:
            self.breaks = input("Enter type of breaks: ")
            if self.breaks.isalpha():
                variable2 = True
            else:
                print("\n Breaks must be a string")
        self.file.write("Breaks: "+ self.breaks)
        self.file.write("\n")


        number = input("Enter cc: ")
        n = len(number)

        while n != 3:
            print(" invalid ")
            number = int(input("Enter cc: "))

        else:

            self.cc = number
            self.file.write("cc: " + self.cc)

        self.file.write("\n")

        variable3 = False
        while not variable3:
            self.brand = input("Enter brand: ")
            if self.brand.isalpha():
                variable3 = True
            else:
                print("\n Brand must be a string")
        self.file.write("Brand: "+self.brand)
        self.file.write("\n")

        variable4 = False
        while not variable4:
            self.chasis = input("Enter Chasis details: ")
            if self.chasis.isalpha():
                variable4 = True
            else:
                print("Chasis details must be a string")
        self.file.write("Chasis Details: "+self.chasis)
        self.file.write("\n")

        self.file.close()

        main_menu()

    def Displaybikelist(self):
        """Displaying the bike list"""
        self.file = open('textfile.txt', 'r')
        print(self.file.read())
        self.file.close()
        main_menu()

    def delete_bikedetails(self):
        """Deleting list"""
        self.file = open('textfile.txt', 'r+')
        self.file.truncate()
        print(self.file.read())
        print("Deleted all Records")
        self.file.close()
        main_menu()



    def search_bike(self):
        """Searching the bike"""
        self.userid = input("Enter the Bike name to be searched: ")
        self.file = open('textfile.txt', 'r')
        self.reading = self.file.read()
        if self.userid in self.reading:
            print("Bike Found")
        else:
            print("Not Found")
        self.file.close()
        main_menu()

    def search_name(self):
        """hi"""
        self.userid = input("Enter the Name of bike to be searched: ")
        self.file = open('textfile.txt', 'r')
        self.reading = self.file.read()
        if self.userid in self.reading:
            print("Record with given name Found")
        else:
            print("Not Found")
        self.file.close()
        main_menu()

    def search_chasis(self):
        """chasis details"""
        self.userid = input("Enter the record to be searched: ")
        self.file = open('textfile.txt', 'r')
        self.reading = self.file.read()
        if self.userid in self.reading:
            print("Chasis details Found")
        else:
            print("Not Found")
        self.file.close()
        main_menu()

    def search_brand(self):
        """search _brand"""
        self.userid = input("Enter the brand of the bike to be searched: ")
        self.file = open('textfile.txt', 'r')
        self.reading = self.file.read()
        if self.userid in self.reading:
            print("Brand name searched is found")
        else:
            print("Not Found")
        self.file.close()
        main_menu()


def main_menu():
    """nope"""
    bikerecords = Bikerecords()
    task = ""

    while(1):
        print("Select task to be performed ")
        print("\n1. Add a Bike Details")
        print("2. Delete Bike details")
        print("3. Search for a Bike details using Name of the bike: ")
        print("4. Display Records")
        print("5. Search for a Record by giving Name: ")
        print("6. Search for a Record by giving Chasis No: ")
        print("7. Search for a Record by giving Brand : ")
        print("8. Exit Records")

        task = int(input("Enter task "))

        if task == 1:
            print("\nEnter Bike Details: ")
            bikerecords.add_bikedetails()


        elif task == 2:
            print("\nRemove An Existing Record ")
            bikerecords.delete_bikedetails()
            break

        elif task == 3:
            print("\nSearch for a Record")
            bikerecords.search_bike()
            break

        elif task == 4:
            print("\nDispaly Records List")
            bikerecords.Displaybikelist()
            break

        elif task == 5:
            print("\nSearch for a Record")
            bikerecords.search_name()
            break

        elif task == 6:
            print("\nSearch for a Record")
            bikerecords.search_chasis()
            break

        elif task == 7:
            print("\nSearch for a Records")
            bikerecords.search_brand()
            break
        else:
            print("\nProgram ended successfully")
            break

if __name__ == '__main__':
    main_menu()

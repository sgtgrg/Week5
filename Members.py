# Base class UniversityMember represents common attributes shared by all university members
class UniversityMember:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID
    # Method to display basic information
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.ID}"

# Student inherits from UniversityMember and adds academic focused attributes
class Student(UniversityMember):
    def __init__(self, name, address, age, ID, academic_record):
        # Call parent constructor (super) to reuse common attributes
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record
    # Override display_info() to include academic record
    def display_info(self):
        return super().display_info() + f", Academic Record: {self.academic_record}"

# Academic inherits from UniversityMember and adds salary & tax code
class Academic(UniversityMember):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        return super().display_info() + f", Tax Code: {self.tax_code}, Salary: {self.salary}"

# GeneralStaff inherits from UniversityMember and adds pay rate & tax code
class GeneralStaff(UniversityMember):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        return super().display_info() + f", Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}"

# This block runs only when the file is executed directly
if __name__ == "__main__":
    student1 = Student("Saugat", "10 Waterson St", 25, "S2518", "A+")
    academic1 = Academic("Prof.Seth", " 12 Royal Oak St", 45, "A2510", "TX101", 75000)
    staff1 = GeneralStaff("Sam", "14 Hobson St", 35, "G63", "TX223", 30)

    print(student1.display_info())
    print(academic1.display_info())
    print(staff1.display_info())

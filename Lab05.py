#Assignment
class person:
    
    def __init__(self,name,age,):
        self.name = name
        self.age = age
        self.__salary=0
        self.address=""
        self.phone_number=""
    
    def update_contact_info(self, address, phone_number):
        self.address = address
        self.phone_number = phone_number
    
    def have_birthday(self):
        self.age+=1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old.")

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Phone Number:", self.phone_number)
        if self.age>=18:
            print("You are an adult!")
        else:
            print("You still a minor")

    def salary(self, salary):
        self.__salary = salary

    def show_salary(self):
        return self.__salary
    
    def greet(self):
        print(f"Name of student is {self.name} and {self.age} old")

    @staticmethod
    def adult(age):
        return age>=18
    

class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    
    def greet(self):
        print(f"Name of student is {self.name} and {self.age} old, student ID : {self.student_id}")

def introduce(person):
    person.greet()

print("\nAssignment 1\n")
#assignment 1
Person = person("O'por", 19)
print(f"Hello my name is {Person.name} and I am {Person.age} old")

print("\nAssignment 2\n")
#assignment 2
Person.greet()

print("\nAssignment 3\n")
#Assignment 3
Person.update_contact_info("KMITL","0875165164")
Person.display_info()

print("\nAssignment 4\n")
#Assignment4
Person=person("Opor",17)
Person.have_birthday()
Person.display_info()

print("\nAssignment 5\n")
#assignment 5
student = student("Tang", 17, "66011627")
student.display_info()
print(f"Student ID: {student.student_id}")

print("\nAssignment 6\n")
student.greet()

print("\nAssignment 7\n")
Person.salary(5000)
print(f"Salary: {Person.show_salary()}")

print("\nAssignment 8\n")
print(Person.adult(20))
print(Person.adult(17))

print("\nAssignment 9\n")
introduce(Person)
introduce(student)
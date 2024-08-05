#Assignment 1,2,3,4
class person:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
        self.__salary=0
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
  
Person = person("O'por", 19)
Student=student("Vachiravith",19,66011627)
introduce(Person)
introduce(Student)


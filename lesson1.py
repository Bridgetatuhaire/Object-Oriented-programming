# A class starts with a capital letter and in a singular form
# A class has attributes
# def __init__() is the constructor used in OOP
#Classes always have methods 

class Student:
    # student_number
    # Name
    # Email
    # Contact
    # age
    # cohort
    def __init__(self,student_number, name, email, contact, age, cohort):
         self.student_number = student_number
         self.name = name
         self.email = email
         self.contact = contact
         self.age = age
         self.cohort = cohort

   #string representation of an object

    def __str__(self):
        return  f'{self.name}, {self.contact}'

    def name_email_cohort(self):
        return f'{self.name}, {self.email}, {self.cohort}'
    
    

#CREATING AN OBJECT/INSTANCE
# Each object has the same attributes form the class
student1 = Student('2023/DSCE/0019/SS', 'Bridget Atuhaire', 'bridgetatuhaire0@gmail.com', '+256783787391', '26', 'three')
print(student1)
print (student1.name_email_cohort())
class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id):
        super().__init__(name, age, cid_number)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} (Student ID: {self.student_id}) is studying hard.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject):
        super().__init__(name, age, cid_number)
        self.subject = subject

    def teach(self):
        print(f"{self.name} (Subject: {self.subject}) is teaching.")

# Creating objects
student1 = Student("Tashi winger Dorji", 20, "S123", "STU001")
teacher1 = Teacher("Ugyen Namgay Phuntsho", 35, "T456", "Math")

# Introduce the student and teacher
student1.walk()
student1.talk()
student1.eat()
student1.sleep()

teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()

# Perform specific actions
student1.study()
teacher1.teach()

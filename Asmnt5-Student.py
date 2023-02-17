#Implement the Complete Student Class

class Student:

    def __init__(self,__name,__rollNumber):
        self.__name = __name
        self.__rollnumber = __rollNumber

    def setName(self,__name):
        self.__name = __name
    
    def getName(self):
        return self.__name

    def setRollNumber(self,__rollNumber):
        self.__rollNumber = __rollNumber

    def getRollNumber(self):
        return self.__rollNumber
    
    Student = Student("yadhu",22)

    print(Student.getName())
    print(Student.getRollNumber())


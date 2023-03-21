#사람 (Super) 클래스를 이용하여 학생들의 정보와 성적을 확인 하는 클래스를 생성하시오

#This is class for having personal information
# Attributes: 
# This will have two arguments:
#  1) Name
#  2) Age
# Method: 
#  1) get_myName()
#  2) get_myAge()
class Person:
    #Person will be created when name and age are given
    def __init__(self, name, age):
        self.myname = name
        self.myage = age
    #print ex) Name: Jaesung
    #          Age: 50 
    def __str__(self):
        return "Name: " + self.myname +"\nAge: " + str(self.myage)
    
    #Pre: None
    #Method: getting name attribute of Person class
    #Output: return name
    def get_myName(self):
        return self.myname
    #Pre: None
    #Method: getting age attribute of Person class
    #Output: return age
    def get_myAge(self):
        return self.myage

#This is the class for setting and getting student information
# Attributes: 
# This student object will have three arguments:
#  1) Person
#  2) Math Grade 
#  3) English Grade 
# Method: 
#  1) set_math_grade(self, math_grade) -> None:
#  2) set_English_grade(self, Eng_grade) -> None:
#  3) get_grade_average(self) -> int:
#     ... etc 
#
# Requirement:
# When print student information please set below format
#
''' Name: 
    Age: 
    Math Grade:
    English Grade:
'''

class Student(Person):
    total = 0
    # create Student object with Person, Math grade, English grade
    def __init__(self, Person, math_grade, eng_grade):
        self.math_grade = math_grade
        self.eng_grade = eng_grade
        self.myage =Person.myage
        self.myname= Person.myname
        Student.total += 1

      




   
    # set math score 
    def set_math_score(self, math_grade):
        self.math_grade = math_grade
      

    # set english score 
    def set_English_score(self, Eng_grade):
        self.eng_grade = Eng_grade
       
    # get math score 
    def get_myName(self):
        return self.myname
    

    # get math score 
    def get_myAge(self):
        return self.myage

       

        
    # get math score 
    def get_math_score(self):
        return self.math_grade
    # get english score 
    def get_english_score(self):
        return self.eng_grade
    #get average score 
    def get_score_average(self):
        return (self.math_grade+self.eng_grade)//2
            

    #print student information 
    def __str__(self):
        return "Name:"+self.myname+"\nAge"+str(self.myage)

        

        

## This is how to use class ##
p1 = Person("Steve Jobs", 25)
p2 = Person("Liam Lee", 50)
p3 = Person("Seokyul Yoon", 60)

## Create student test score 
std1 = Student(p1,  80, 90)
std2 = Student(p2, 100, 100)
std3 = Student(p3, 0, 0)

## print student information 
print(std1)
print(std2)
print(std3) 

print("\n ***************************")
## change score of student 
std3.set_English_score(10)
std3.set_math_score(20)
print(std3.get_myName(), ": ", "\nMath: ", std3.get_math_score(), " and English: ", std3.get_english_score())

print("\n ***************************")
## get average score of each student 
print(p1.get_myName() + " test score average: ", std1.get_score_average())
print(p2.get_myName() + " test score average: ", std2.get_score_average())
print(p3.get_myName() + " test score average: ",std3.get_score_average())

print("\n ***************************")

#How many student we have 
if Student.total < 1:
    print("we have one student")
elif Student.total > 1:
    print("we have ", Student.total, " students")
else:
    print("we don't have student here")

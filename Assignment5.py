class School:

    def __init__(self, students):
        self.__students__ = students
    
    def student(self,surname):
        return f"{surname} is in year {self.__students__[surname]}"

elever = {'bob':4,'per':23}


kth = School(elever)

print(kth.student('bob'))

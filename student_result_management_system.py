import weakref 
class Classroom:
    _students=[] 
    def __init__(self,name,std,rollno):
        self.name=name 
        self.std=std 
        self.rollno=rollno 
        self.__class__._students.append(self) 
    @classmethod
    def display(cls):
        for i in cls._students:
            print(i.name) 
    @classmethod
    def delete(cls,std):
        cls._student.remove(std)
        print(std.name+"is removed from classrrom")
        del std 

    @classmethod
    def search(cls,rno):
        for i in cls._students:
            if i.rollno==rno:
                print("Roll Number {} is {}".format(rno,i.name))
                break 
std1=Classroom("Poojitha",10,6)
std2=Classroom("Prabhas",8,7)
std3=Classroom("Prassu",10,9)
Classroom.display()
Classroom.search(1)

from Student import Student

class OverseasStudent(Student):
    # override printGpa in student class
    def printGpa(self):
        if(self.gpa > 3.5):
            print("優秀")
        else:
            print("良好")
    def isOverseas(self):
        print("True")
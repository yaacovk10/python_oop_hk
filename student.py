class Student:
    def __init__(self, name, age, studies):
        self.name= name
        self.age = age
        self.studies = studies
        self.year = 0
        self.average = 0
        self.coefs = 0



    def exam(self, score):
        """
        Add the exam score to average. In this implementation, exam coefficient is 3
        """
        self.average = ((score * 3) + (self.average * self.coefs))/(self.coefs +3)
        self.coefs += 3
        

    def exercise(self, score):
        """
        Add the exercise score to average. In this implementation, exercise coefficient is 1
        """
        self.average = (score + (self.average * self.coefs) ) /(self.coefs + 1)
        self.coefs += 1
        
    def _average(self):
        """
        Return average score of student
        """
        return self.average
        

    def course(self, course):
        """
        In this example each year there are 4 courses. When student completes 1 course, his progression is 0.25
        """
        self.year += course * 0.25

    def _progression(self):
        return self.year
    

# Test cases
student1 = Student("Alice", 20, "Computer Science")
student1.exam(90)
student1.exercise(85)
student1.course(2)
print(f"{student1.name} - Average: {student1._average()} Progression: {student1._progression()} years")

student2 = Student("Bob", 22, "Mathematics")
student2.exam(75)
student2.exercise(92)
student2.course(3)
print(f"{student2.name} - Average: {student2._average()} Progression: {student2._progression()} years")






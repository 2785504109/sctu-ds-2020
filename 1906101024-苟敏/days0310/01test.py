class Student():
    def __init__(self,name,age,score):
        self.name=name 
        self.age=age 
        self.score=score

    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_score(self):
        print(max(self.score))
s=Student("王小明",20,[90,99,80])
s.get_name()
s.get_age()
s.get_score()
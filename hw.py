
class Kids:
    def __init__(self,name,  age, gender, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

    #getters
    def get_age(self):
        return self.age

    #setters
    def set_age(self, new_age):
        self.age = new_age

    def showKids (self):
        print("hello, I am {} with {}, {}, {}". format(self.name, self.age, self.gender, self.grade))


    

k1 = Kids("logan", "12", "male", "grade 8")
k2 = Kids("alice", "14", "female", "grade 9")

k1.showKids()


print(k2.grade)

print(k1.gender)

#class - getters get the properties, setters set new values



#object-what it does(function) and how it looks(property) oops-object oriented programming structure
#class is blue print of object - contains properties and functions of an object/objects

class Fruits:
    def __init__(self, color, taste, shape):
        self.color = color
        self.taste = taste
        self.shape = shape

    #getters
    def get_shape(self):
        return self.shape

    #setters
    def set_shape(self, new_shape):
        self.shape = new_shape

    def showFruit(self):
        print("hello, I am fruit with {}, {}, {}". format(self.color, self.taste, self.shape))


    

lemon = Fruits("yellow", "bitter", "rugby")
greenapple = Fruits("green", "sour", "spherical")

greenapple.set_shape("round")

lemon.showFruit()


print(greenapple.shape)

print(lemon.taste)

#class - getters get the properties, setters set new values



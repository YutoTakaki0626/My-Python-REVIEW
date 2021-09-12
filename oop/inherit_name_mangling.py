class Person:
    def __init__(self, name):
        self.name = name
        self.mymethod()

    def mymethod(self):
        print('Person method is called')

    #__mymethod = mymethod

class Baby(Person):
    def mymethod(self):
        print('Baby method is called')

taro_baby = Baby('Taro')
taro_baby.mymethod()
class Human():
    fName = ''
    lName = ''
    dob = ''
    createdObject = ''
    
    def __init__(self,firstname,lastname,dob):
        self.fName = firstname
        self.lName = lastname
        self.dob = dob
        self.createdObject = 'now'
    def __str__(self):
        return self.fName + ' ' + self.lName + ' ' + self.dob + ' ' + self.createdObject
    def eat(self):
        return 'We all humans eat food'
    def walk(self):
        return 'We all humans walk'
class Baby(Human):
    momName = ''
    dadName = ''
    def __init__(self, mom, dad,firstname,lastname,dob):
        super().__init__(firstname,lastname,dob)
        self.momName = mom
        self.dadName = dad
    def __str__(self):
        return f'Baby`s name is {self.fName} {self.lName}, parent`s name are {self.momName} and {self.dadName} and wasborn in {self.dob}'
    def eat(self):
        return 'I`m a baby I only drink milk'
    def walk(self):
        return 'I`m a baby I can`t walk yet'
 
        
humano1 = Human('Ernesto', 'Figueredo','21-06-85')
print(humano1.eat())
print(humano1.walk())
print(humano1)

baby1 = Baby('Ceci','Ernesto','Enrique','Figueredo','26-04-2021')
print(baby1)
print(baby1.eat())
print(baby1.walk())


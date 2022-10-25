class Employee:
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    
    def __str__(self):
            return f'Employee is {self.firstName} {self.lastName} and is earning {self.salary}'
        
    def giveRaise(self, salary):
        self.salary = salary
    
class Developer(Employee):
    def __init__(self, firstName, lastName, salary, programmingLanguages):
        super().__init__(firstName, lastName, salary)
        self.programmingLanguages = programmingLanguages
        
    def addLanguage(self, language):
        self.programmingLanguages.append(language)
    
    def __str__(self):
            languageString = ''
            for i in range(len(self.programmingLanguages)):
                if i == 0:
                    languageString = self.programmingLanguages[i]
                else:
                    languageString += ', ' + self.programmingLanguages[i]
                 
            return f'Employee is {self.firstName} {self.lastName} and is earning {self.salary} his skills are {languageString}'
        
employee1 = Employee('Albert','Wesker',100000)
print(employee1)
employee1.giveRaise(150000)
print(employee1)

dev1 = Developer('Ernesto','Figueredo','120000',['Python','JS','PHP'])
print(dev1)
dev1.giveRaise(200000)
print(dev1)
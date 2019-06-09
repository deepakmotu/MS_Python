class employee:
    def __init__(self, first, last):
        print('Initialization')
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def fullname(self):
        print('Setting Fullname')
        return f'{self.first} {self.last}'

    @property
    def email(self):
        print('Setting Email')
        return f'{self.first}.{self.last}@gmail.com'

    @email.setter
    def email(self, email):
        print('Setting new Email')
        first, last = email.split('@')
        self.first = first
        self.last = last


emp = employee('Deepak', 'Gupta')

emp.first='Aarav'
emp.email='deepak@gmail'

print(emp.email)
print(emp.first)
print(emp.last)
print(emp.fullname)

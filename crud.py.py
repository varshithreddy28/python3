class patient:
    def __init__ (self,name,age,i,check):
        self.name=name
        self.age=age
        self.i=i
        self.check=check
    def chek(self):
        print(f'Name of patient ---> {self.name}')
        print(f'Age of the patient ---> {self.age}')
        print(f'ID of the patient  ---> {self.i}')
        if self.check == '+':
            print('The patient is suffering with Corona positive')
        elif self.check == '-':
            print('The patient is with Corona Negative')
        elif (self.check == 'd' or self.check == 'D'):
            print('Sorry! the patient has died! :/')
name=input('Enter name of the patient : ')
age=int(input('Enter age of the patient : '))
i=input('Enter ID of the patient : ')
check=input('Enter the State of the patient [+/-] : ')
p=patient(name, age, i, check)
d=1
while True:
    print('1.Check patient details')
    if d==1:
        print('2.Modify patient condition')
    while True:
        try:
            opp=int(input('Enter the option : '))
        except:
            print('Opps u didnt entered an integer')
        else:
            break
    if opp==1:
        p.chek()
    elif opp==2:
        check=input('Enter the State of the patient [+/-] or patient died [d/D] : ')
        p=patient(name, age, i, check)
        if check=='d' or check=='D':
            d=0
    else:
        print('Invaild choise')
    c=input('Do you want to do any thing else [y/n]  :')
    if c=='y':
        print('Select your choise  : ')
    else:
        print('STAY HOME STAY SAFE...')
        break
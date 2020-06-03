class Bank:
    def __init__ (self,owner,bal):
        self.owner=owner
        self.bal=bal
    def ow(self):
        return print(f'The name of account holder is {self.owner}')
    def ba(self):
        return print(f'The balance in the account is {self.bal}')
    def de(self,d):
        self.bal=self.bal+d
        return print(f'the balance in the account is {self.bal}')
    def wit(self,w):
        if (w<self.bal):
            self.bal=self.bal-w
            return print(f'The balance in the account is {self.bal}')
        else:
            return print(f'The amount in the account is insuffient')
    def check(self):
        print(f'The Account details are : ')
        print(f'Name of account holder : {self.owner}')
        print(f'Balance in the account : {self.bal}')
n=input('Enter name of account holder')
bl=int(input('Enter balance in the account'))
b=Bank(n,bl)
while True:
    print('Choose the option : ')
    print('1.Deposite money')
    print('2.Withdrawl money')
    print('3.Account enquirey')
    c=int(input('Choose your option'))
    if c==1:
        d=int(input('Enter depoisite ammount'))
        b.de(d)
    elif c==2:
        w=int(input('Enter money wanted to withdrawl'))
        b.wit(w)
    elif c==3:
        b.check()
    else:
        print('Invanid choise')
    print('Do you want to try again')
    c=input('Enter your choise [yes/no]')
    if c=='yes':
        print('Enter data again')
    else:
        print('Thank You! Visit Again')
        exit()

def display(my):
    print(f' {my[7]}|{my[8]}|{my[9]}')
    print('-------')
    print(f' {my[4]}|{my[5]}|{my[6]}')
    print('-------')
    print(f' {my[1]}|{my[2]}|{my[3]}')
def choise():
    ch1=input('Enter your choise X or O')
    if ch1=='x' :
        ch2='o'
        return ('x','o')
    elif ch1=='o':
        ch2='x'
        return ('o','x')
    else:
        print('In valid choise : ')
        ch1=input('Enter choise again')
        if ch1=='x':
            ch2='o'
            return ('x','o')
        else:
            return ('o','x')
def opp(ch1,ch2,my,i):
    p=int(input('Select your choise player 1 : '))
    if my[p]==' ':
        my[p]=ch1
        display(my)
        check(ch1,ch2,my)
    else:
        print('The position has alraedy taken')
        p=int(input('Select your choise player 1 : '))
        if my[p]==' ':
            my[p]=ch1
            display(my)
            check(ch1,ch2,my)
            exit()
    if i==0:
        q=int(input('Select your choise palyer 2 : '))
        if my[q]== ' ':
            my[q]=ch2
            display(my)
            check(ch1,ch2,my)
        else:
            print('The position has already taken')
            q=int(input('Enter your choise player 2 : '))
            if my[q]==' ':
                my[q]=ch2
                display(my)
                check(ch1,ch2,my)
                exit()
    return my
def check(ch1,ch2,my):
    if (my[1]==my[2]==my[3]==ch1) or (my[4]==my[5]==my[6]==ch1) or (my[7]==my[8]==my[9]==ch1):
        print('-----Player 1 won the match!!-----')
        exit()
    elif (my[1]==my[4]==my[7]==ch1) or (my[2]==my[5]==my[8]==ch1) or (my[3]==my[6]==my[9]==ch1):
        print('-----Player 1 has won the match-----')
        exit()
    elif (my[1]==my[5]==my[9]==ch1)or(my[3]==my[5]==my[7]==ch1):
        print('-----Player 1 has won the match-----')
        exit()
    elif (my[1]==my[2]==my[3]==ch2) or (my[4]==my[5]==my[6]==ch2) or (my[7]==my[8]==my[9]==ch2):
        print('-----Player 2 has won the match-----')
        exit()
    elif (my[1]==my[4]==my[7]==ch2) or (my[2]==my[5]==my[8]==ch2) or (my[3]==my[6]==my[9]==ch2):
        print('-----Player 2 has won the match-----')
        exit()
    elif (my[1]==my[5]==my[9]==ch2) or (my[3]==my[5]==my[7]==ch2):
        print('-----Player 2 has won the match-----')
        exit()
my=[' ']*10
lis=[0,1,2,3,4,5,6,7,8,9]
print('Welcome to TIK-TAK-TO game')
print('Please check our Board and enter the choise ')
display(lis)
ch1,ch2=choise()
print(f'The choise of palyer 1 is : {ch1}')
print(f'The choise of player 2 is : {ch2}')
print('Please select your choise between 1 to 9')
i=0
opp(ch1,ch2,my,i)
opp(ch1,ch2,my,i)
opp(ch1,ch2,my,i)
opp(ch1,ch2,my,i)
i=i+1
opp(ch1,ch2,my,i)
print('OPPS! The match has tied')
exit()

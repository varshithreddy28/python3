import datetime
import winsound
def extend(am):
    t=int(input('1 minute or 5 minutes [1/5]'))
    if t==1:
        am=am+1
    elif t==5:
        am=am+5
        print(am)
    return am
ah=int(input('Enter wake up hour'))
am=int(input('Enter wake up minute'))
ap=input('am or pm')
if ap=='pm':
    ah=ah+12
while True:
    if ah==datetime.datetime.now().hour and am==datetime.datetime.now().minute:
        print('Wake up The time is up')
        dur=10000 #millysec
        freq=400 #hz
        winsound.Beep(freq,dur)
        c=input('Do you want to extend time[yes/no]')
        if c=='yes':
            et=extend(am)
        else :
            print('Wake up')
        while True:
            if ah==datetime.datetime.now().hour and et==datetime.datetime.now().minute:
                print('Wake up man wake up ')
                dur=10000 #millysec
                freq=400 #hz
                winsound.Beep(freq,dur)
                break
        break
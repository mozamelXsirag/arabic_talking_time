import time
import winsound

currentTime = time.strftime("%H:%M")
time_list = currentTime.split(':')
hour = int(time_list[0])
minit = time_list[1]
x = int(minit[0])
y = int(minit[1])


def sayhour():

    global hour
    if hour > 12:
        hour -= 12
    audio='hour/'+str(hour)+'.wav'
    winsound.PlaySound(audio, winsound.SND_ALIAS)


def check_minit_x():
    if x != 0:
        audio='x/'+str(x)+'.wav'
        winsound.PlaySound(audio, winsound.SND_ALIAS)


def check_minit_y():
    audio='y/'+str(y)+'.wav'
    if (y == 1):
        if (x == 1):
            winsound.PlaySound('y/eleven_y.wav', winsound.SND_ALIAS)

        elif (x > 1):
            winsound.PlaySound(audio, winsound.SND_ALIAS)

        elif(x == 0):
            winsound.PlaySound('y_minit_y.wav', winsound.SND_ALIAS)


    elif (y == 2) :
        if(x == 1):
            winsound.PlaySound('y/twelve_y.wav', winsound.SND_ALIAS)

        elif(x > 1):
            winsound.PlaySound('y/'+str(y)+'.wav', winsound.SND_ALIAS)

        elif(x ==0):
            winsound.PlaySound('y/two_minits_y.wav', winsound.SND_ALIAS)
    elif(y>2):
        winsound.PlaySound(audio, winsound.SND_ALIAS)


def minit_minits():
    if int(minit)>=3 and int(minit)<=10:
        winsound.PlaySound('statements/minits.wav', winsound.SND_ALIAS)
    elif int(minit)>=11 and int(minit)<=59:
        winsound.PlaySound('statements/minit.wav', winsound.SND_ALIAS)


def main():
    winsound.PlaySound('statements/hour.wav', winsound.SND_ALIAS)
    sayhour()
    if x+y!=0:
        winsound.PlaySound('statements/and.wav', winsound.SND_ALIAS)
    check_minit_y()
    if y != 0 and x > 1:
        winsound.PlaySound('statements/and.wav', winsound.SND_ALIAS)

    check_minit_x()
    minit_minits()



if __name__ == '__main__':
    main()











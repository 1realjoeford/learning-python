message = ''
started = False
while True:
    message = input('> ').lower()
    if message == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game''')
    elif message == 'start':
        if started == False:
            print('car started')
            started = True
        else:
            print('Car is already started')
    elif message == 'stop':
        if started ==  True:
            print('car has stopped')
            started = False
        else:
            print('car is already stopped')
    elif message == 'quit':
        break
    else:
        print('I dont understand that ...')

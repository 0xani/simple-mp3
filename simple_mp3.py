import os
import glob


def intro():
    print('-------------------------------------------------------------------')
    print('Welcome to simple-mp3.')

    print('This is a low resource mp3-player.')
    print("If your short on ram or speed, this won't slow down your computer.")


def mp3_lst():
    mp3_lst = []
    for mp3 in glob.glob('Music/*.mp3'):
        mp3_lst.append(mp3)
    return mp3_lst
        
def menu(mp3s):
    if len(mp3s) == 0:
        input('Music folder is empty. Add some songs to get rockin!')
    else:
        print("Please select from the following:")
        i = 0
        print('ID:')
        for mp3 in mp3s:
            print(f'{i}: {mp3}')
            i += 1

    
def simple_mp3():

    mp3s = mp3_lst()


    done = False

    while not done:
        menu(mp3s)
        try:
            if len(mp3s) == 0:
                usr = input("Add some songs to simple-mp3/Music to get rockin! Enter (Q) to (Q)uit")
                done = parse_input(usr)                
            else:
                usr = input('Number or (S)top or (Q)uit : ')
                done = parse_input(usr)
                if not done and usr.lower() != 's':
                    choice = int(usr)
                    play_music(mp3s, choice)
                elif usr.lower() == 's':
                    print('Stopping Music')
                else:
                    input('GOODBYE . . .')
        except:
            print(f'ERROR. Looks like you entered a song number not in range 0 - {len(mp3s)}')
        


def parse_input(usr):
    if usr.lower() == 's':
        os.system('killall afplay')
        return False
    elif usr.lower() == 'q':
        return True
    else:
        return False
        
        
def play_music(mp3s, choice):
    bash_command = 'afplay -q high ' + '"' + mp3s[choice] + '" &'
    print(bash_command)
    os.system(bash_command)

def outro():
    print('See ya later!')
    print('-------------------------------------------------------------------')
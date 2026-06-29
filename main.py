from alarm_locig import AlarmClock
from tkinter import *

root = Tk()
root.geometry('500x300')


def start_program():

    user_time = alarm_entry.get()
    alarm_entry.delete('0', END)

    if my_clock.set_alarm(user_time) == False:
        info_label.config(text='Incorrect format')
    else:
        my_clock.set_alarm(user_time)
        my_clock.turn_on()
        my_clock.check_alarm(root)
        info_label.config(text=f'Alarm set for {user_time}')


def stop_program():

    my_clock.turn_off()
    info_label.config(text='alarm stopped')

def click_choose_sound():
    my_clock.choose_sound()
    info_sound_label.config(text=my_clock.sound_file)


my_clock = AlarmClock('?.mp3')

alarm_label = Label(root, text='Alarm time:')
alarm_label.pack()

alarm_entry = Entry(root)
alarm_entry.pack()

alarm_button = Button(root, text='start alarm', command=start_program)
alarm_button.pack()

alarm_stop_button = Button(root, text='stop alarm', command=stop_program)
alarm_stop_button.pack()

info_label = Label(root, text='')
info_label.pack()

ghost_label1 = Label(root, text='')
ghost_label1.pack()

ghost_label2 = Label(root, text='')
ghost_label2.pack()

choose_sound_button = Button(root, text='choose sound', command=click_choose_sound)
choose_sound_button.pack()

info_sound_label = Label(root, text='not sound selected')
info_sound_label.pack()

root.mainloop()
from tkinter import *
import datetime
from tkinter import messagebox
from tkinter import filedialog
import os

root = Tk()
root.geometry('500x300')

alarm_time = ''
alarm_running = False


def start_alarm():
    global alarm_time, alarm_running

    alarm_time = alarm_entry.get()
    alarm_entry.delete(0, END)

    parts = alarm_time.split(':')

    if len(alarm_time) != 5:
        info_label.config(text='invalid time format, example: HH:MM')
        return

    if alarm_time[2] != ':':
        info_label.config(text='use the HH:MM format')
        return

    if not parts[0].isdigit() or not parts[1].isdigit():
        info_label.config(text='hours and minutes must contain only numbers')
        return

    if int(parts[0]) > 23 or int(parts[1]) > 59:
        info_label.config(text='invalid hours or minutes')
        return

    alarm_running = True
    info_label.config(text='the countdown has begun')
    check_alarm()


def check_alarm():
    global alarm_running
    
    if not alarm_running:
        return

    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%H:%M")

    if current_time_str == alarm_time:
        os.startfile(sound_path)
        alarm_running = False
    else:
        root.after(1000, check_alarm)


def stop_alarm():
    global alarm_running
    alarm_running = False
    info_label.config(text='alarm stopped')


sound_path = ''

def choose_sound():
 global sound_path
 sound_path = filedialog.askopenfilename(
     filetypes=[
        ('Audio files', '*.wav *.mp3'),
        ('All files', '*.*')
    ]
 )
 
 info_sound_label.config(text=sound_path)
 


alarm_label = Label(root, text='Alarm time:')
alarm_label.pack()

alarm_entry = Entry(root)
alarm_entry.pack()

alarm_button = Button(root, text='start alarm', command=start_alarm)
alarm_button.pack()

alarm_stop_button = Button(root, text='stop alarm', command=stop_alarm)
alarm_stop_button.pack()

info_label = Label(root, text='')
info_label.pack()

ghost_label1 = Label(root, text='')
ghost_label1.pack()

ghost_label2 = Label(root, text='')
ghost_label2.pack()

choose_sound_button = Button(root, text='choose sound', command=choose_sound)
choose_sound_button.pack()

info_sound_label = Label(root, text='not sound selected')
info_sound_label.pack()

root.mainloop()
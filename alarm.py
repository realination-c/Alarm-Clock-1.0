from tkinter import *
import datetime
from tkinter import messagebox
from tkinter import filedialog
import os


class AlarmClock:


    def __init__(self, sound_file):
        self.sound_file = sound_file
        self.is_active = False
        self.alarm_time = ''
    

    def is_valid_time(self, user_time):
       
        parts = user_time.split(':')

        if len(parts) != 2:
           return False
        if not parts[0].isdigit() or not parts[1].isdigit() :
           return False
        if int(parts[0]) > 23 or int(parts[1]) > 59:
           return False
        else:
           return True
      

    def set_alarm(self, user_time):
        
        if self.is_valid_time(user_time):
            self.alarm_time = user_time
        else:
            info_label.config(text='!!!')

        
    def turn_on(self):
        self.is_active = True


    def turn_off(self):
        self.is_active = False
        info_label.config(text='alarm stopped')

    
    def  check_alarm(self):

        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime('%H:%M')

        if self.is_active and current_time_str == self.alarm_time:
            os.startfile(self.sound_file)
            self.is_active = False
        else:
            root.after(1000, self.check_alarm)

    def choose_sound(self):

        sound_path = filedialog.askopenfilename(
            filetypes=[
                ('Audio files', '*.wav'),
                ('Audio files', '*.mp3'),
                ('All files', '*.*')
                ]
        )
        self.sound_file = sound_path
        info_sound_label.config(text=self.sound_file)
    


def start_program():
    user_time = alarm_entry.get()
    my_clock.set_alarm(user_time)
    my_clock.turn_on()
    my_clock.check_alarm()



root = Tk()
root.geometry('500x300')

my_clock = AlarmClock('?.mp3')

alarm_label = Label(root, text='Alarm time:')
alarm_label.pack()

alarm_entry = Entry(root)
alarm_entry.pack()

alarm_button = Button(root, text='start alarm', command=start_program)
alarm_button.pack()

alarm_stop_button = Button(root, text='stop alarm', command=my_clock.turn_off)
alarm_stop_button.pack()

info_label = Label(root, text='')
info_label.pack()

ghost_label1 = Label(root, text='')
ghost_label1.pack()

ghost_label2 = Label(root, text='')
ghost_label2.pack()

choose_sound_button = Button(root, text='choose sound', command=my_clock.choose_sound)
choose_sound_button.pack()

info_sound_label = Label(root, text='not sound selected')
info_sound_label.pack()

root.mainloop()
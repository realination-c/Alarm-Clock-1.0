
import datetime
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
            return True
        else:
            return False

        
    def turn_on(self):
        self.is_active = True


    def turn_off(self):
        self.is_active = False

    
    def  check_alarm(self, root):

        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime('%H:%M')

        if self.is_active and current_time_str == self.alarm_time:
            os.startfile(self.sound_file)
            self.is_active = False
        else:
            root.after(1000, lambda: self.check_alarm(root))

    def choose_sound(self):

        sound_path = filedialog.askopenfilename(
            filetypes=[
                ('Audio files', '*.wav'),
                ('Audio files', '*.mp3'),
                ('All files', '*.*')
                ]
        )
        self.sound_file = sound_path

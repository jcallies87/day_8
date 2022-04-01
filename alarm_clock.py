

class Alarm_Clock:
    def __init__(self, time , on_off, alarm):
        self.alarm_clock_time = time
        self.alarm_clock_alarm = on_off
        self.alarm_time = alarm

    def set_clock(self):
        self.alarm_clock_time = input("what time do you want to set the clock to?")
        print(f"The current time is {self.alarm_clock_time}.")
    
    def turn_alarm_on(self):
        self.alarm_clock_alarm = True

    def turn_alarm_off(self):
        self.alarm_clock_alarm = False
    
    def set_alarm(self):
        self.alarm_time = input("What time would you like the alarm set to?")
        print(f"Alarm is now set to {self.alarm_time}.")

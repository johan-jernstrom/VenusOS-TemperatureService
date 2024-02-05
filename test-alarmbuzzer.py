#!/usr/bin/env python
import time
from alarmbuzzer import AlarmBuzzer 
alarmBuzzer = AlarmBuzzer()

time.sleep(30)  # wait for 30 seconds to allow time for pressing the button and testing the buzzer


# print("------- TEST CASE: Button press silences all buzzers for 20 seconds but not a third one -------")
# alarmBuzzer.CheckTemp(12, 10, 1)
# alarmBuzzer.CheckTemp(12, 10, 2)
# time.sleep(3)
# alarmBuzzer.SilenceAllActiveAlarms()
# alarmBuzzer.CheckTemp(12, 10, 1)
# alarmBuzzer.CheckTemp(12, 10, 2)
# time.sleep(5)
# alarmBuzzer.CheckTemp(12, 10, 3)
# time.sleep(5)
# print("Done")


# print("------- TEST CASE: Button press silences the first buzzer for 20 seconds but not the second one -------")
# alarmBuzzer.CheckTemp(12, 10, 1)
# time.sleep(3)
# alarmBuzzer.SilenceAllActiveAlarms()
# time.sleep(3)
# alarmBuzzer.CheckTemp(12, 10, 2)
# time.sleep(5)
# print("Done")

#------- TEST CASE: Button press and normal temperature silence the buzzer -------
# alarmBuzzer.CheckTemp(12, 10, 1)
# time.sleep(5)
# alarmBuzzer.CheckTemp(12, 10, 1)  # should not buzz since it is already buzzing
# time.sleep(5)
# alarmBuzzer.SilenceAllActiveAlarms() # should silence the buzzer
# time.sleep(5)
# alarmBuzzer.CheckTemp(8, 10, 1)   # should not buzz since temperature is normal, and also make it immediately buzz if temperature goes high again
# alarmBuzzer.CheckTemp(12, 10, 1)  # should buzz since temperature is high
# time.sleep(5)
# alarmBuzzer.CheckTemp(8, 10, 1)   # should stop buzzing since temperature is normal
# time.sleep(5)
# print("Done")
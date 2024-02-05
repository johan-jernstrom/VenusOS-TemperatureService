#!/usr/bin/env python
import logging
import time
from gpiozero import Buzzer, Button

class AlarmBuzzer:

    # buzzerPin = 20 #38 is GPIO20
    # buttonPin = 16 #36 is GPIO16
    def __init__(self, buzzerPin = 20, buttonPin = 16):
        self.logger = logging.getLogger(__name__) # create logger
        
        self.buzzer = Buzzer(buzzerPin) # set up buzzer
        self.button = Button(buttonPin, hold_time=3) # set up button
        self.button.when_pressed = self.SilenceAllActiveAlarms
        self.button.when_held = self.test_buzzer

        self.ActiveAlarmsDict = {}    # dictionary to keep track of sensors that are currently active
        self.SensorSilenceTime = 30*60 # seconds to keep sensor silent after it has been activated

    def test_buzzer(self):
        if self.buzzer.is_active:
            self.logger.info("Buzz already active")
            return
        self.buzzer.beep(on_time=.25, off_time=.25, n=None, background=True)    # start same buzz as in CheckTemp to test the buzzer
    
    def SilenceAllActiveAlarms(self):
        self.logger.info("Silencing all active alarms")
        self.buzzer.off()
        self.buzzer.beep(on_time=1, off_time=1, n=1, background=True)   # beep once to indicate that all active alarms have been silenced
        # set all time values in dict to current time meaning all currentlu active sensors will be turned off for X seconds
        for key in self.ActiveAlarmsDict:
            self.ActiveAlarmsDict[key] = time.time()
            self.logger.info("Sensor " + str(key) + " has been turned off for " + str(self.SensorSilenceTime) + " seconds")

    def CheckTemp(self, temp, highTempAlarm, sensorId = "0"):
        self.logger.debug("Checking temperature " + str(temp) + " with highTempAlarm " + str(highTempAlarm) + " for sensor " + str(sensorId))
        # check if temp, highTempAlarm or sensorId is None or empty string 
        if temp is None or highTempAlarm is None or sensorId is None or temp == "" or highTempAlarm == "" or sensorId == "":
            self.logger.debug("AlarmBuzzer: temp, highTempAlarm or sensorId is None or empty string")
            return
        try:
            temp = float(temp)
            highTempAlarm = float(highTempAlarm)
        except:
            self.logger.error("AlarmBuzzer: Error converting temp " + str(temp) + " or highTempAlarm " + str(highTempAlarm) + " to float")
            return

        if temp > highTempAlarm:
            self.logger.info("High temperature alarm for sensor " + str(sensorId))

            # check dictory value for sensorId and if it is there then check if it is within self.SensorSilenceTime seconds
            if sensorId in self.ActiveAlarmsDict and time.time() - self.ActiveAlarmsDict[sensorId] < self.SensorSilenceTime:
                self.logger.debug("Sensor " + str(sensorId) + " has already started buzz within " + str(self.SensorSilenceTime) + " seconds")
                return
            
            # add sensorId to dict with current time
            self.ActiveAlarmsDict[sensorId] = time.time()
            self.logger.info("Sensor " + str(sensorId) + " has high temperature")

            # start buzz on separate thread unless it is already started
            if self.buzzer.is_active:
                self.logger.info("Buzz already active")
                return
            self.buzzer.beep(on_time=.25, off_time=.25, n=None, background=True)
        else:
            self.logger.debug("Sensor " + str(sensorId) + " has normal temperature")
            if sensorId in self.ActiveAlarmsDict:
                self.ActiveAlarmsDict.pop(sensorId)   # remove sensorId from dict if temperature is normal to make it buzz if temperature goes high again
                self.logger.info("Sensor " + str(sensorId) + " has returned to normal temperature")
                # if no sensor is buzzing then turn off the buzzer
                if len(self.ActiveAlarmsDict) == 0:
                    self.buzzer.off()
                    self.logger.info("Buzzer has been turned off since no sensor is active")

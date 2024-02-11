## Venus OS Temperature Service
### Fork from Rikkert-RS VenusOS-TemperatureService 
This is a service to publish temperature type data onto the DBus of VenusOs running on a Raspberry Pi device.  
Note: Currently this will not display the CPU temperature on Venus GX, only on RPi.

Added Support to install this with Kevin Windrem's Venus OS Setup Helper (https://github.com/kwindrem/SetupHelper)
### Fork from LHardwick Victron-Service
In this fork, in addition to displaying temperatures, a buzzer is connected and activated for an audible alarm if the temperature goes above a defined max value.
A button os also connected to silence the alarm.

NOTE: The install process and integration with SetupHelper is NOT yet testet or completed. I only added roughly what is needed in the current scripts but havent had time to start testing it out. Doubt it will work in the current form. 
Therefore, the install is currently made by manually adding and modifying the files on the RPi after installing the unmodified version of VenusOS-TemperatureService made by Rikkert-RS... 
Future ambition is to test and modify also the install process in order to achieve a fully automated install. 

## INSTALL INSTRUCTIONS
No Settings needed for 1 Wire (e.g. DS18B20) all you need is to install SetupHelper and configure a custom Package.
  - Package name: VenusOS-TemperatureService
  - GitHub user: jernstrom-johan
  - GitHub Tag: latest

      ### Screenshots
      <details><summary>Add Custom Package</summary>

      ![PackageManager Menü](/screenshots/PackageManagerMenu.png)
      ![Add Custom Package ](/screenshots/PackageManagerAddPackage.png)
      ![Fill Custom Package](/screenshots/PackageManagerAddCustomPackage.png)
      ![Install Package](/screenshots/PackageManagerInstallAktivPackage.png)

</details>

### Enabled Features in this Setup:
  - Raspberry Pi CPU temperature
  - 1-Wire Support (Temperatures) Data Port GPIO 26 on RPi
  
    Please keep in mind that there can always be conflicts with the GPIO's. Depending on what hardware you have (CAN hat etc)
    The 1Wire GPIO Port can be adjusted in u-boot/config.txt after install

### Can be activated but not tested (in dbus-i2c.py)
  - i2c Sensors
  - ADC Sensors

Tested on Rasberry 3+ with Venus OS 2.91

### Own Services:
 Note, only services of path type "Temperature" will be displayed on the console and VRM
 If you modify the service to pubish data as a path that is of a different type
 it will only be available via the DBus and will not appear on the console or VRM.

![Temps in Venus OS Menu](/screenshots/TempsInMenu.png)

Hope this all works for you

Rikkert-RS

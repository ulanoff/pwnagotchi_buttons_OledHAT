# Description
Scripts for buttons of Waveshare Oled HAT (any with joystick and 3 buttons)
I'm very bad in English:(
## POWRS.py - Shutdown and reboot by key1 (PIN 21). 
Pressing key1 leads to rebooting system. Pressing key1 for more then 1.5 seconds leads to shutdown.
## poweroffgpio21.py - Shutdown system by clicking key1. 
You can change GPIO_PIN = 21 to another one.
## rebootauto.py - restarts pwnagotchi in auto mode. 
GPIO_PIN = 20 (key2).
## reboomanual.py - restarts pwnagotchi in manual mode.
GPIO_PIN = 16 (key3).
## detrue - sets deauth mode to true (check if this mode is legal in ur country).
Finds deauth-false string in config.toml, changes it and restart pwnagotchu.
## defalse - sets deauth mode to false (100% legal)
Finds string with enabled deauth mode and changes it to false, then restarts pwnagotchi.
# Installing scripts. 
1. Put them wherever u want. I recommend to put them in -> /home/pi/ dir.
2. Run -> sudo nano /etc/rc.local
3. Before "exit 0" add line like this -> python /home/pi/NAMEOFSCRIPT.py
## Run 2 or more scripts. 
1. Just add "&" after 1 script command in rc.local and add another script. 
For example ->

python /home/pi/detrue &
python /home/pi/defalse &
python /home/pi/POWRS
2. Save and exit.
3. GLHF!

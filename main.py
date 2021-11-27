import os

from gpiozero import LED, MotionSensor

pir = MotionSensor(4)
led = LED(17)

pir.wait_for_motion()
print("You moved")
led.on()
os.system('omxplayer -o alsa:hw:1,0 music.mp3')
pir.wait_for_no_motion()
led.off()

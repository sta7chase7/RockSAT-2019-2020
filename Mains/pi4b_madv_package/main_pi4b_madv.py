#Electrical note: if all MADV commands are currently executable by completing a circuit, how can this be accomplished on a coding level with a Pi?

options = """Also: unless something sensible can be made of the MADV selfie stick PCB [who got that?], we will need to include a relay in the electrical box. [Ths might be a good application for the ]

A third option could be to check the voltage change for MADV trigger instances, then basically wire a Pi's GPIO pins into the circuit loop [may require voltage stepping to avoid breaking a Pi].

With the right documentation, any of these instances is a route to us having software control over the MADV."""

import RPi.GPIO as GPIO

#Start main on boot

#all things here to be executed in bash?
#If so, do we need main_pi4b to be .sh?

#send "power on" signal to MADV
#-Specify mode based on MADV terminal timings

#Send "start recording" signal to MADV

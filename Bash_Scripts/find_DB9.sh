#Look for something along the lines of
#

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"
        [[ "$devname" == "bus/"* ]] && continue
        eval "$(udevadm info -q property --export -p $syspath)"
        [[ -z "$ID_SERIAL" ]] && continue
        echo "/dev/$devname - $ID_SERIAL"
    )
done

#use the /dev address for PuTTY
#Settings;
#Baud: 19200
#Data Bits: 8
#Stop bits: 1
#Parity: None
#Flow Control: ?
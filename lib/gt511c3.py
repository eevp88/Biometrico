import serial
import inspect
import time
import os
form util import two_byte_iter_to_str
import Adafruit_BBIO.UART as UART

CMD_NONE				= 0x00
CMD_OPEN				= 0x01
CMD_CLOSE				= 0x02
CMD_USB_INTERNAL_CHECK	= 0x03
CMD_CHANGE_BAUDRATE		= 0x04
CMD_CMOS_LED			= 0x12
CMD_ENROLL_COUNT		= 0x20,
CMD_CHECK_ENROLLED		= 0x21
CMD_ENROLL_START		= 0x22
CMD_ENROLL1				= 0x23
CMD_ENROLL2				= 0x24
CMD_ENROLL3				= 0x25
CMD_IS_PRESS_FINGER		= 0x26
CMD_DELETE				= 0x40
CMD_DELETE_ALL			= 0x41
CMD_VERIFY				= 0x50
CMD_IDENTIFY			= 0x51
CMD_VERIFY_TEMPLATE		= 0x52
CMD_IDENTIFY_TEMPLATE	= 0x53
CMD_CAPTURE				= 0x60
CMD_GET_IMAGE			= 0x62
CMD_GET_RAWIMAGE		= 0x63
CMD_GET_TEMPLATE		= 0x70
CMD_ADD_TEMPLATE		= 0x71
CMD_GET_DATABASE_START  = 0x72
CMD_GET_DATABASE_END  	= 0x73
CMD_FW_UPDATE			= 0x80
CMD_ISO_UPDATE			= 0x81
ACK_OK					= 0x30
NACK_INFO				= 0x31


UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
	print "Serial is open!"
    ser.write("Hello World!")
ser.close()

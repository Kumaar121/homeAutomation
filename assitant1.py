import smbus2
import bme280
import smtplib as s
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
from time import sleep
import l293d.driver as l293d
from pulsesensor import Pulsensor
import datetime
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.clear()

SERIAL_PORT = "/dev/ttyS0"#since we have rpi3 ||"/dev/ttyAMA0"   Raspberry Pi 2
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
setup()
ser.write("AT+CMGF=1\r") # set to text mode
time.sleep(3)

print("....................................WELCOME TO YOUR ASSISTATNT ...............................")
print("                     ...........KINDLY SWITCH ON THE POWER BUTTON ...........")

print("......SIR KINDLY CHECK READINGS OF THE PARAMETERS ON SERIAL MONITOR ......")
p = Pulsensor()
p.startAsyncBPM()
while True:
    h_beat = p.BPM
    if h_beat > 0:
        print("BPM: %d" % h_beat)
    else:
        print("No Heartbeat found")
p.stopAsyncBPM()
motor1 = l293d.motor(22,18,16)
motor2 = l293d.motor(15,13,11)
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

temp = bme280.sample(bus, address, calibration_params)

print(temp.temperature)


flag=0
#supppse the temp is 100 DEG FAH , 

temp=102
h_beat=120

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

def main():
    name=input("Enter your name - ")
    Age=int(input("Enter your Age -")
    ID=int(input("Enter your ID - ")
    Temp=int(input("Enter the body temperature - ")
    h_beat=int(input("Enter the heart beat - "))
    temp1()

def reading1():
    if(temp > 100 and temp < 98  or h_Beat>100 and h_beat<60):
        print("--Need To be diagnosed --")
        question()
    else:
        print("Temperature and Heartbeats are normal")
        question1()
        
def question1():
    #tell me other factors u want me to include 





def question():
    print("---Kindly Answer the following questions----\n")
    q1=input("What you ate last night ??\n")
    q2=int(input("At what time you slept ??\n"))
    q3=input("Do you have sore throat ??\n")
    q4=input("Do you have back pain ??\n")
    q5=input("Are you feeling depressesd ??\n")
    print("---Diagnose complete---\n")
    #time.sleep(0.5)
    gen_report()
    #send_report()
    
def send_report():
    ob=s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("wic8932@gmail.com","Sk@123")
    filename = "Doctor1.txt"
    f = file(filename)
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    ob.sendmail("wic8932@gmail.com","shivamdarknight121@gmail.com","HELLO -shivam")
    ob.close()
    validate()
def validate():
    #code for telling medicince prescribed by the doctor

    
    assistance()
            
def assistance():
    #kindly check the medicine dispenser it will start opening
    for i in range(0,150):
        motor1.clockwise()
        motor2.clockwise()
    l293d.cleanup()
    GPIO.output(8, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(5, GPIO.HIGH)
    sendMessage()
def sendMessage():
    #send message to the doctor that medicine is taken
    t = str(datetime.datetime.now())
    ser.write('AT+CMGS="9994429705"\r')
    time.sleep(3)
    msg = "Sending status at " + t
    print "Sending SMS with status info:" + msg
    ser.write(msg + chr(26))
    lcd.message = "PILL IS TAKEN"
    
    
    
def gen_report():
    if((q3=='yes' and q4=='yes' and q5=='yes') and temp>100):
        f=open("Doctor1.txt","w+")
        f.write("This is the report of the concerned patient the details are as follows prescribe the medicine \n")
        f.write("Name - %s\n"%name)
        f.write("Age -%d\n"%Age)
        f.write("ID -%d\n"%ID)
        f.write("h_beat -%d\n"%h_beat)
        f.write("Temp -%d\n"%temp)
        send_report()
        
    
    

    
    


    

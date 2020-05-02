#import smbus2
#import bme280
#port = 1
#address = 0x76
body="Kindly check the patient report"
print("....................................WELCOME TO YOUR ASSISTATNT ...............................")
print("                     ...........KINDLY SWITCH ON THE POWER BUTTON ...........")

print("......SIR KINDLY CHECK READINGS OF THE PARAMETERS ON SERIAL MONITOR ......")


#bus = smbus2.SMBus(port)
#calibration_params = bme280.load_calibration_params(bus, address)
# the sample method will take a single reading and return a
# compensated_reading object
#data = bme280.sample(bus, address, calibration_params)

#print(data.temperature)


flag=0
#supppse the temp is 100 DEG FAH , 

temp=102
h_beat=120
def main():
    name=input("Enter your name - ")
    Age=int(input("Enter your Age -")
    ID=int(input("Enter your ID - ")
    Temp=int(input("Enter the body temperature - ")
    h_beat=int(input("Enter the heart beat - "))
    temp1()

def temp1():
    if(temp > 100 and temp < 98  or h_Beat>100 and h_beat<60):
        print("--Need To be diagnosed --")
        question()
    else:
        print("Temperature and Heartbeats are normal")
        question1()
        
def question1():





def question():
    print("---Kindly Answer the following questions----\n")
    q1=input("What you ate last night ??\n")
    q2=int(input("At what time you slept ??\n"))
    q3=input("Do you have sore throat ??\n")
    q4=input("Do you have back pain ??\n")
    q5=input("Are you feeling depressesd ??\n")
    print("---Diagnose complete---\n")
    report()
    
def report():
    if((q3=='yes' and q4=='yes' and q5=='yes') and temp>100):
        print("You are suffering from mild cold , we are sending your report to the doctor\n")
        ob.sendmail("wic8932@gmail.com","shivamdarknight121@gmail.com","HELLO RAJESH -shivam")
        assistance()
def assistance
    


    

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input('Enter a hour:-'))
print(hour)

if(hour >= 0 and hour < 12):
    print("Good Morning Sir/Maam")
elif (hour >= 12 and hour <=17):
    print("Good Afternoon Sir/Maam")
elif(hour >=17 and hour < 0):
    print("Good Evening Sir/Maam")
elif(hour >=24):
    print("Wrong Time, Please Correct Time Between 0 to 24")
else:
    print("Good Night Sir/Maam!")




    
    
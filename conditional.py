# import time
# name = input("Enter your name:").title()
# print(name)
# currentTime = time.strftime('%H:%M:%S')
# print(currentTime)
# hours = int(time.strftime("%H"))
# if(hours>=4 and hours<=12):
#     print("Good Morning, Sir", name)
# elif(hours>=12 and hours<=16):
#     print("Good Afternoon, Sir")
# elif(hours>=16 and hours<=20):
#     print("Good Evening, Sir")
# else:
#     print("Good Night, Sir")



# 4-12 Morning Time
# 12-15 Afternoon Time
# 16-19 Evening Time
# 20-24 Night Time

import time

a = input("Enter your name:").title()
print(a)
currentTime = time.strftime('%H:%M:%S')
print(currentTime)
hours = int(time.strftime("%H"))
if (hours >= 4 and hours <= 12):
  print("Good Morning,", a)
elif (hours >= 12 and hours <= 16):
  print("Good Afternoon, Sir")
elif (hours >= 16 and hours <= 20):
  print("Good Evening, Sir")
else:
  print("Good Night, Sir")

  
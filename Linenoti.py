import requests
import random
import time
def Line() :
    url = 'https://notify-api.line.me/api/notify'
    token = '7AwvBfvzcQzWYp8jlKKJIs0Hg7P3Pa00o5q1AwuV2Tn'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    otp = 0
    i = 0
    
    
    otp = random.randrange(100000,999999)

    print (otp)
    msg = otp
    r = requests.post(url, headers=headers, data = {'message':msg})
    
    #for i in range(6) :
     #   reotp[i] = input("Enter OTP : ")
#
 #       if reotp == otp :
  #          print("Welcome")
    time.sleep(15)

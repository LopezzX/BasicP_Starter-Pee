import time
x = int(input("ระยะทาง = "))
v = 0.07
if x <= 4:
    time.sleep(1)
    print("ราคา = ","Free")
elif x >= 5  and x <= 50:
    time.sleep(1)
    print("ราคา = ",10,"baht")
    print("ยอดรวม + vat7% = ", v * 10 + 10 ,"บาท")
elif x >= 51  and x <= 100:
    time.sleep(1)
    print("ราคา = ",15,"baht")
    print("ยอดรวม + vat7% = ", v * 15 + 15 ,"บาท")
elif x >= 101  and x <= 300:
    time.sleep(1)
    print("ราคา = ",25,"baht")
    print("ยอดรวม + vat7% = ", v * 25 + 25 ,"บาท")
elif x >= 301  and x <= 500:
    time.sleep(1)
    print("ราคา = ",35,"baht")
    print("ยอดรวม + vat7% = ", v * 35 + 35 ,"บาท")
else :
    time.sleep(1)
    print("ราคา = ",45,"baht")
    print("ยอดรวม + vat7% = ", v * 45 + 45 ,"บาท")


#vat 7
#รวม 
weight = (input("น้ำหนัก"))
high = (input("ส่วนสูง"))
weight = float(weight)
high = float(high)
t = (high*high)
BMI = (t/weight)
print ("%.2f" %BMI)
if BMI < 18.50:
    print("น้ำหนักน้อย/ผอม")
elif BMI >= 18.50 and BMI <= 22.90:
    print("ปกติ(สุขภาพดี)")
elif BMI >= 23 and BMI <= 24.90:
    print("ท้วม/โรคอ้วนระดับ 1")
elif BMI >= 25 and BMI <= 29.90:
    print("อ้วน/โรคอ้วนระดับ 2")
else:
    print("อ้วนมาก/โรคอ้วนระดับ 3")


















def prod(n):
    sum_price = 0
    for i in range(n):
        #price = int(input("ราคาสินค้า %d:"%(i+1)))
        price = int(input(f"ราคาสินค้า{i+1}:"))
        sum_price += price
    return sum_price

def tax (total):
    vat = (7/100)*total
    return



num = int(input("จำนวนรายการสินค้า"))
total = prod(num)

print(f"ราคารวม { total }")
print(f"ภาษีมูลค่าเพิ่ม %.2f" % (tax(total)))
net_price = total + tax(total)
print("รวมเป็นเงินทั้งสิน %.2f" % net_price)
money = int(input("จำนวนเงิน:"))
print("เงินทอน %.2f" % (chage(money, net_price)))



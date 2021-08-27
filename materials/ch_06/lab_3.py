'''
ราคารถยนต์ 100,000 บาท
ผ่อนรถยนต์เป็นเวลา 12 เดือน
อัตราดอกเบี้ย 3% ต่อเดือน

ดอกเบี้ย = เงินต้น * อัตราดอกเบี้ย * ระยะเวลาในการผ่อน
       = 100000 * (0.03) * 12
       = 36,000

ยอดหนี้ = เงินต้น + ดอกเบี้ย = 100000 + 36000 = 136,000

ยอดชำระรายเดือน = ยอดหนี้ / ระยะเวลาในการผ่อน = 136000 / 12 = 11,333.34
'''

deposit = float(input('Enter the car deposit: '))
month = int(input('Enter the installment time (month): '))

if month == 12:
    int_rate = 0.01
elif month == 24:
    int_rate = 0.015
elif month == 36:
    int_rate = 0.025
else:
    int_rate = None

if int_rate is None:
    print('Installment time must be 12, 24 or 36 month')
else:
    int_total = deposit * int_rate * month
    debt = deposit + int_total
    pay_per_month = debt / month
    print(f'You have to pay {pay_per_month:.2f} Baht/month')

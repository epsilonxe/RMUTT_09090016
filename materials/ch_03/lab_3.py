'''
โปรแกรมคำนวณอายุปัจจุบัน (เบื้องต้น)
ไม่มีการใช้ control statement
ไม่มีการใช้ไลบรารี datetime
กำหนดให้ 1 เดือนมี 30 วัน
'''

# วันปัจจุบัน Date of Present
# ตรงนี้สามารถใช้ไลบรารี datetime ในการหาวันปัจจุบันได้ครับ (ยังไม่ได้กล่าวถึง)
p_day = 1
p_month = 8
p_year = 2021
print('Date of present (D/M/Y) is  ', p_day, '/', p_month, '/', p_year)

# วันเกิด Date of Birth
b_day = int(input('Enter your day of birth: '))
b_month = int(input('Enter your month of birth: '))
b_year = int(input('Enter your year of birth: '))

# วันอ้างอิง (ใช้ในการคำนวณจำนวนวัน)
# กำหนดให้เป็นวันที่ 1 มกราคม 1900
ref_day = 1
ref_month = 1
ref_year = 1900

# คำนวณจำนวณวันนับจาก "วันอ้างอิง" ถึง "วันเกิด"
b_days_from_ref = (b_year - ref_year) * 365 + (b_month - ref_month) * 30 + (b_day - ref_day)

# คำนวณจำนวณวันนับจาก "วันอ้างอิง" ถึง "วันปัจจุบัน"
p_days_from_ref = (p_year - ref_year) * 365 + (p_month - ref_month) * 30 + (p_day - ref_day)

# คำนวณอายุเป็นจำนวนวัน
days_age = (p_days_from_ref - b_days_from_ref)

# คำนวณอายุเป็นปี-เดือน-วัน
years = days_age // 365  # หารปัดเศษเพื่อหาจำนวนปีก่อน
days_remainder = days_age % 365  # เศษวันที่เหลือจากการหาจำนวนปี

months = days_remainder // 30  # หารปัดเศษเพื่อหาจำนวนเดือน
days = days_remainder % 30  # เศษวันที่เหลือจากการหาจำนวนเดือน

print('Your age is ', days_age, 'days')
print('Your age is ', years, 'years', months, 'months', days, 'days')

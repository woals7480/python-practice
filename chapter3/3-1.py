money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")

# 한 줄 표현 가능
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
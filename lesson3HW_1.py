import random
num = random.randint(1,10)
ans = 0

i = 0

while ans != num:
   ans = input('1到10猜一個數字?')
   ans = int(ans)
   
   if ans != num: 
    print('你猜錯了')
    print('在猜一次')
   elif ans == num :
    print('你猜對了,恭喜')
    
   else:
    print('你答對了')
   i = i + 1
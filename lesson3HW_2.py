import random
num = random.randint(1,20)
num = int(num)
ans = 0

i = 0
while i < 5:
 ans = input('1到20猜一個數字?')
 ans = int(ans)
 
 if i < 4 and num > ans:
   print('太小,再猜一次')

 elif i < 4 and num < ans:
   print('太大,再猜一次')
 elif num != ans:
   print('五次都猜錯了')
 
 else:
   print('你答對了')
   print('答案是', ans)
   break   
 
 i = i + 1
s = int(input('請輸入你的成績'))

num = int(input('請猜成績'))

while num != s:
    if num > s:
        num = int(input('低一點'))
    else:
        num = int(input('高一點'))
else:
    print('答對了')		

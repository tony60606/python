'Loop迴圈：如果條件成立,則重複執行迴圈內的程式碼'
A = 0 
while A <= 10 :
    print(A)
    A += 1
print('-'*20)
'Q1：接收密碼'
password = 1234 
num = int(input('請輸入四位數密碼：'))
time = 1 
while num != password :
    if time < 3 :
        print('密碼輸入錯誤')
        num = int(input('請重新輸入'))
        time += 1
    else :
        print('錯誤超過3次已上鎖,請與技術人員連絡')
        break
print('成功登入')
print('-'*20)
'Q2：猜密碼'
import random 
ans = random.randint(1,100)
gusse = int(input('請猜一個1~100之間的數字：'))
while gusse != ans :
    if gusse > ans :
        print('你猜得太大拉,再猜一次吧')
        gusse = int(input('請猜一個1~100之間的數字：'))
    else :
        print('你猜得太小拉,再猜一次吧')
        gusse = int(input('請猜一個1~100之間的數字：'))
print('恭喜猜對啦')
print('答案是',ans)
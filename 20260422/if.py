'python 中的條件判斷只有 if'
'1.單層if'
A = 10 
if A <= 20 :
    print(A)
'2.兩項條件if...else'
age = int(input('請輸入您的年紀：')) 
if age >= 18 :
    print('已成年')
else :
    print('您未成年')
'3.多項條件if...elif...else'
'條件區間的寫法： 1. xxx > ooo and xxx < @@@'
grade = int(input('請輸入等級分：'))
if grade >= 90 :
    print('S+')
elif grade < 90 and grade >= 80 :
    print('S')
elif grade < 80 and grade >= 70 :
    print('A+')
elif grade < 70 and grade >= 60 :
    print('A')
else :
    print('B')
'條件區間的寫法： 2. ooo < xxx < @@@ => 不建議'
ml = int(input('請輸入ml數：'))
if 600 < ml :
    print('特大杯',ml ,'ml')
elif 480 < ml <= 600 :
     print('大杯', ml,'ml')
elif 360 < ml <= 480 :
     print('中杯', ml,'ml')
else :
     print('小杯',ml,'ml')

'Q1：判斷成績'
score = int(input('請輸入學生成績：'))
if score >= 60 :
    print('恭喜你,及格囉')
    if score > 90 :
        print('A+')
    elif score >= 81 and score <= 90 :
        print('A')
    elif score >= 71 and score <= 80 :
        print('B')
    elif score >= 61 and score <= 70 :
        print('B-')
    else :
        print('C')
else :
    print('本次考試不及格,請再接再厲')
    if score >= 51 and score <= 59 :
        print('C')
    elif score >= 41 and score <= 50 :
        print('D')
    else :
        print('E')
'Q2：年齡劃分'
age2 = int(input('請輸入您的年紀：'))
if age2 < 12 :
    print('分類為兒童')
elif age2 >= 12 and age2 < 18 :
    print('分類為青少年')
elif age2 >= 18 and age2 < 30 :
    print('分類為青年')
else :
    print('分類為社會人士')
'Q3：季節分類'
month = int(input('請輸入現行月份：'))
if month in [2,3,4] :
    print('現在是',month,'月,為春天')
elif month in [5,6,7] :
    print('現在是',month,'月,為夏天')
elif month in [8,9,10] :
    print('現在是',month,'月,為秋天')
elif month in [11,12,1] :
    print('現在是',month,'月,為冬天')
else :
    print('請輸入正確月份格式')
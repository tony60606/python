#變數：代表一個名稱關聯一個or一組值
A = 100
print(A)
#算術函數：+(加)、-(減)、*(乘)、/(除)、//(整數除：取商數)、%(整數除：取餘數)、**(平方)
B = 10
C = 6
print(B+C)
print(B-C)
print(B*C)
print(B/C)
print(B//C)
print(B%C)
print(B**C)
#指定函數：+=(加後賦值)、-=(減後賦值)、*=(乘後賦值)、/=(除後賦值)、//=(整除賦值：取商數)、%=(整除賦值：取餘數)
D = 150
D += 15
print(D)
D -= 20
print(D)
D *= 20
print(D)
D /= 3
print(D)
D //= 30
print(D)
D %= 9
print(D)
#比較符號：>、>=、<、<=、!=、==
E = "王"
F = "許"
G = 99
H = 80
print(E>F)
print(E>=F)
print(H<G)
print(H<=G)
print(F!=H)
print(E==G)
# 邏輯符號：and、or、not
# and：條件皆符合為true，有一方不符合則為false
# or：條件皆符合或其中一方符合為true，雙方皆不符合則為false
# not：將判斷結果相反，即排除 => 只需要一個條件 => 寫法： not(條件)
I = "董"
J = "鄭"
K = "劉"
L = "黃"
print(I>J and K<L)
print(I>=K or J<=L)
print(not(K==L))

import random


def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)
#函數 get_int(訊息字串、最小值、預設值)
#    line 為 訊息字串
#    如果 line 和 預設值 不是 無，回到 預設值 的狀態
#    如果 預設值 為None(未設定預設值)， i 為訊息字串的數字型態(如果訊息字串無法轉換成數字將引發 ValueError 例外)
#    如果 i 小於 最小值 ，顯示出 "must be >= " 最小值
#    ValueError  例外為錯誤，顯示出 err

rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)

#執行 get_int 函式 輸入符合設定的 行數 、 列數 、最小值

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)

#設定 預設值為 1000
#如果 預設值 小於 最小值， 預設值 為 2倍的 最小值
#執行 get_int 函式 輸入符合設定的 最大值
				  
row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1

#當　行數　大於　行 時執行
#    line 為 空字串
#    列 為 0
#    當 column 小於 columns 時執行
#        產生 i 為介於最小值與最大值的隨機數
#        s 為 i 的字串型態
#        當 S 為小於 10 的數 ，在數字之前加入一個空白字串
#        將產生出的隨機數字加入 line 中 列數 +1 
#    顯示出 line 
#    將行數+1


#此程式為產生一個網狀的隨機整數



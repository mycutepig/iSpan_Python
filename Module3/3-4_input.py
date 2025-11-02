# input() 函數 讓使用者在終端機輸入資料

# 取得使用者輸入的資料
user_inpiut = input("請輸入數字: ")
print(user_inpiut)
print(type(user_inpiut))


# 將使用者輸入強制轉型成 int
user_inpiut = int(user_inpiut)
print(type(user_inpiut))
if user_inpiut > 10:
    print("num 大於 10")

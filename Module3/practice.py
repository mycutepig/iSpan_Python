# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」
import random
password = random.randint(1, 100)
maximum = 100
minimum = 1

guess = int(input(f"Enter a integer from {str(minimum)} ~ {str(maximum)}: "))
while guess != password:
    if guess > maximum or guess < minimum:
        print("超出範圍請重新輸入")
    elif guess > password:
        maximum = guess
        print("請輸入更小的數字")
    else:
        minimum = guess
        print("請輸入更大的數字")
    guess = int(input(f"Enter a integer from {str(minimum)} ~ {str(maximum)}: "))
        

print("恭喜中獎")













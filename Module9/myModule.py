def get_discount(price, discount):
    discount_index = price // 2000

    if price >= 2000:
        price -= discount * discount_index
    
    return price

print(__name__)

# 測試模組
# 很重要!!! 只在這個檔案 執行
if __name__ == "__main__":
    data = [
        {
            "total": 6000,
            "discount": 200
        },
        {
            "total": 8000,
            "discount": 200
        }
    ]

    for d in data:
        answer = get_discount(d["total"], d["discount"])
        print(f"折扣後的金額: {answer} 元")



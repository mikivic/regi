# 商品の価格リスト
menu = {
    "モスバーガー": 440,
    "モスチーズ": 480,
    "テリヤキチキン": 450,
    "スパイシーモス": 480,
    "ダブルモス": 600,
    "テリヤキバーガー": 430
}

# 合計金額を計算する関数
def calculate_total(items):
    total = 0
    for item, quantity in items.items():
        if item in menu:
            total += menu[item] * quantity
    return total

# おつりを計算する関数
def calculate_change(total_price, amount_paid):
    change = amount_paid - total_price
    return change

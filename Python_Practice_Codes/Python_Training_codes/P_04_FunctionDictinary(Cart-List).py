import copy
cart = [
    {"name": "苹果", "price": 5.5,  "qty": 3},
    {"name": "牛奶", "price": 12.0, "qty": 1},
    {"name": "面包", "price": 8.5,  "qty": 2},
    {"name": "泡面", "price": 3.0,  "qty": 5},
    {"name": "牛肉", "price": 45.0, "qty": 1},
]
def add_item(cart, item):
    copy_cart = copy.deepcopy(cart)
    copy_cart.append(item)
    return copy_cart
cola = {"name": "可乐", "price":3.5, "qty":2}
new_cart = add_item(cart, cola)
def total_price(cart):
    item_total = 0
    for i in cart:   # 注意使用参数，不要使用外部new_cart
        subtotal = i["price"] * i["qty"]
        item_total += subtotal
    return item_total
def expensive_items(cart, threshold):
    extra = []
    for i in cart:
        if i["price"] >= threshold :
            extra.append(i)
    return extra
print(f"总价: {total_price(cart):.2f}")
print(f"单价 >= 10 的商品: {expensive_items(cart, 10)}")
print() # 以下为是否修改原cart列表测试(题目要求)
print("\n=== 测试：add_item 有无修改原列表 ===")
before = cart.copy()                      # 先存一份原样
new_cart = add_item(cart, {"name": "鸡蛋", "price": 6.0, "qty": 10})

print("原 cart 长度  :", len(cart),      " 期望 5")
print("新 cart 长度  :", len(new_cart),  " 期望 6")
print("原 cart 没被改:", cart == before, " 期望 True")
print("是两个不同列表:", cart is not new_cart, " 期望 True")
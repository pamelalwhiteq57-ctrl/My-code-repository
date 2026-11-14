while True:
    choice = input("请选择（1:摄氏度转华氏度，2:华氏度转摄氏度）：")

    if choice == '1':
        c = float(input("请输入摄氏度："))
        f = c * 1.8 + 32
        print(f"结果：{c}°C = {f}°F")
    elif choice == '2':
        f = float(input("请输入华氏度："))
        c = (f - 32)/1.8
        print(f"结果：{f}°F = {c}°C")
    else:
        print("输入无效，请输入 1 或 2")
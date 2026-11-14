with open("test.txt", "r", encoding="UTF-8") as f:
    for each in f:
        print(each.strip())
# 读
# f.read(n)          # 读 n 个
# f.readline()       # 读一行
# for line in f:     # 逐行（推荐）

# # 写
# f.write(s)         # 写字符串，自己加 \n
# f.writelines(lst)  # 写列表，自己带 \n

# # 定位
# f.tell()           # 当前位置
# f.seek(pos)        # 跳到 pos

# # 收尾
# f.flush()          # 刷盘
# f.close()          # 关闭（with 自动）
class C:
    def __init__(self, data):
        self.data = data
    def __contains__(self, item):
        print("Hello")
        return item in self.data
c: C = C([1, 2 , 3, 4, 5])
print(3 in c)
print()
'''当__contains__未实现。在对象进行同一性运算时，会用__iter__和__next__进行代偿'''
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    # 重写 __contains__
    def __contains__(self, item):
        print(f"🔍 正在底层检查：歌单里有没有《{item}》...")
        # 只要判断 item 是否在列表中即可
        return item in self.songs

my_list = Playlist(["晴天", "七里香", "稻香"])

# 触发 __contains__
print("晴天" in my_list)   
# 输出:
# 🔍 正在底层检查：歌单里有没有《晴天》...
# True

# 触发 __contains__（注意底层依然会触发，但结果取反）
print("告白气球" not in my_list) 
# 输出:
# 🔍 正在底层检查：歌单里有没有《告白气球》...
# True
print()
class D:
    def __bool__(self):
        # 必须返回 True 或 False
        return True
d: D = D()

class MyList:
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        print("触发了 __len__")
        return len(self.data)

m1 = MyList([1, 2])
m2 = MyList([])

print(bool(m1))  # 触发 __len__，返回 2，所以是 True
print(bool(m2))  # 触发 __len__，返回 0，所以是 False
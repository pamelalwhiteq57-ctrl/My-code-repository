origin_tags = ["Python", "学习", "笔记", "Python"]
def make_tagger(start_tags):
    tags_list = start_tags[:]
    def add(new_tags):
        final_list = []
        for i in new_tags:
            if i in tags_list:
                final_list.append(i)
            else:
                tags_list.append(i)  # append,是"就地修改"列表内容,tags_list这个变量本身没被重新赋值,所以不需要nonlocal
        return final_list
    def all_tags():
        return set(tags_list)
    return add, all_tags
add, unique = make_tagger(origin_tags)
print("第一次添加:", add(["Python", "算法", "算法", "数据结构"]))
print("第二次添加:", add(["笔记", "算法", "机器学习"]))
print("累计唯一标签:", unique())
print("原列表没被改:", origin_tags)
print()
# print('''此次训练发现的问题:
# 1.没找到内部函数的参数如何调用，只需让外部函数返回内部函数，再在外面接收之后，就自然是内函数了，也就可以写参数了
# 2.未搞懂列表直接相加的添加元素法和append方法添加法的区别，后者无需nonloacl，∵其是忽略地址原地修改列表内容，
# 而前者是要直接使用它了，这个时候作用域就会出问题
# 3.集合添加元素方法不熟练(虽然最终代码没用到)''')
# Question:22
'''
字符串排序
'''
def sort_string(text:str) -> str:
    return "".join(sorted(text))
def main() -> None:
    user_input = input("输入要排序的字符串:")
    sorted_text = sort_string(user_input)
    return print(f"排序结果: {sorted_text}")
if __name__ == "__main__":
    main()
# Question:32
'''
使用函数递归打印如下菱形图案，(其中第四行左右两端各有一个空格)
    #
   ###
  #####
 ####### 
  #####
   ###
    #
'''
def paint(n1, n2, c):
    print(" " * n1 + "#" * n2)       
    if c == 7:                       
        return
    if c < 4:                        
        paint(n1 - 1, n2 + 2, c + 1)
    else:                            
        paint(n1 + 1, n2 - 2, c + 1)
paint(4, 1, 1)
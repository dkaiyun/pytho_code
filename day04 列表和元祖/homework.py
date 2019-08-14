# 1，写代码，有如下列表，按照要求实现每⼀个功能
#li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#-----------------------------------------------
# li.append("seven")
# li.insert(0,"Tony")
# li[1]="Kelly"
# li.extend(ee)
# s = "qwert"
# li.extend(s)
# li.pop(1)
# del li[1:4]
# li.reverse()
# print(li.count("alex"))

# 2，写代码，有如下列表，利⽤切⽚实现每⼀个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
#---------------------------------
# ee = li[:3]
# print(li[:3])
# print(li[3:6])
# print(li[::2])
# print(ee)
# print(li[1:6:2])
# print(li[-1:])
# print(li[-3:-8:-2])

# 3,写代码，有如下列表，按照要求实现每⼀个功能。
#lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1)将列表lis中的"tt"变成⼤写（⽤两种⽅式）。
# 2)将列表中的数字3变成字符串"100"（⽤两种⽅式）。
# 3)将列表中的字符串"1"变成数字101（⽤两种⽅式）。

# lis[3][2][1][0] = lis[3][2][1][0].upper()
# lis[3][2][1][1] = "100"
# lis[3][2][1][2] = "101"
# print(lis)

# 4,请⽤代码实现：
# li = ["alex", "eric", "rain"]
# 利⽤下划线将列表的每⼀个元素拼接成字符串"alex_eric_rain"
# print(li[0] + "_" + li[1] + "_" + li[2])

# 5.利⽤for循环和range打印出下⾯列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)

# 6.利⽤for循环和range找出100以内所有的偶数并将这些偶数插⼊到⼀个新列表中。
# lst = []
# for i in range(100):
#     b = i%2
#     if int(b) == 0:
#         lst.append(i)
# print(lst)

#7.利⽤for循环和range 找出50以内能被3整除的数，并将这些数插⼊到⼀个新列表中。

# lst = []
# for i in range(50):
#      b = i%3
#      if int(b) == 0:
#          lst.append(i)
# print(lst)

#8.利⽤for循环和range从100~1，倒序打印。
# lst = []
# # for i in range(101):
# #     lst.insert(0,i)
# # print(lst)

#9.利⽤for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，然后对列表的元素进⾏筛选，将能被4整除的数留下来。
# lst = []
# for i in range(10,100):
#       b = i%4
#       if int(b) == 0:
#           lst.insert(0,i)
# print(lst)
#10，利⽤for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个列表，将能被3整除的数改成*。

# lst = []
# for i in range(31):
#     lst.append(i)
#     b = i%3
#     if b ==0:
#         lst[i] = "*"
# print(lst)


#11，查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到⼀个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
# lst = []
# for i in range(len(li)):
#     cc = li[i].replace(' ','')
#     if cc.startswith("A"):
#         lst.append(cc)
#     elif cc.startswith("a"):
#         lst.append(cc)
#     elif cc.endswith("c"):
#         lst.append(cc)
# print(lst)


#15. 敲七游戏. 从0开始数数. 遇到7或者7的倍数要在桌上敲⼀下. 编程来完成敲七
# lst = []
# num7 = input("请输入一个数字:  ")
# for i in range(1,int(num7)):
#     b = i%7
#     if b == 0:
#         lst.append("咣")
#     else:
#         lst.append(i)
# print(lst)

# 16. (升级题) 编写程序. 完成⼼动⼥⽣的筛选. (升级题)
#           ⾸先. 程序会提示⽤户录⼊10位⼼仪⼥⽣的姓名. 然后把10位⼥⽣的名
# 字和序号展示出来. 由⽤户选择⼼动⼥⽣. 此时⽤户可以选择3个⼼动⼥⽣. 把⽤
# 户选中的三个⼼动⼥⽣的名字打印出来. 供⽤户继续选择. 这⼀次选择. 只能选
# 择⼀名⼥⽣. 然后输出⽤户的⼼动⼥⽣是xxx
# for i in range(1,10):
#     b = 10-i
#     gril = input('请输入心动女生的名字(您还可以输入个): ')

















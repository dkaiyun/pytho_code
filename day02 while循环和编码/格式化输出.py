# name = input("请输入你的名字:　")
# age = int(input("你的年龄是多大: "))
# home = input("你来自哪里: ")
#
# print("我叫%s,我来自%s,我今年%s岁了." %(name,home,age,))
# print(f"我叫{name},我来自{home},我今年{age}岁了.")


a = input("输入 :  ")  #输入 4+6+8

a1 = a.split("+")
numa = 0
for i in range(len(a1)):
    numa = int(a1[i]) + numa
print(numa)
# a3 = int(a1[0])+int(a1[1])
# print(a3)

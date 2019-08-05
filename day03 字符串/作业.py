
#
# name1 = name.strip()
# print(name1)
# print(name[0:2])
# print(name[-2:])
# print(name[1:-1])
#
# if name.startswith("al"):
#     print("name de kaitou shi al")
# else:
#     print("name de  kaitou bushi al")
# name = "aleX leNb"
# if name.endswith("Nb"):
#     print("name de jiewei shi Nb")
# else:
#     print("name de  jiewei bushi Nb")
#1.7
# name2 = name.replace("l","P")
# print(name2)
# #1.8
# name3 = name.replace("l","P",1)
# print(name3)
# #1.9
# name4 = name.split("l")
# # print(name4)
#1.10
# name5 = name.split("l",1)
# print(name5)
#1.11
# name6 = name.upper()
# print(name6)
# #1.12
# name7 = name.lower()
# print(name7)
# #1.13
# name8 = name.capitalize()
# print(name8)

# #1.14
# print(name.count("l"))
# #1.15
# print(name.count("l",4))
#1.16
# name9 = name.index("N")
# print(name9)
#1.17
# name10 = name.find("N")
# print(name10)
#1.18
# name11 = name.find("X le")
# print(name11)
#1.19
# print(name[1])
# name = "aleX leNb"
#1.20
# print(name[:3])
#1.21
# print(name[-3:])
# name13 = name.find("e")
# print(name13)
#
# #2
# s = "123a4b5c"
# #2.1
# print(s[:3])
# #2.2
# print(s[3:6])
# #2.3
# print(s[::2])
#2.4
# s4 = s[1:7:2]
# print(s4)
# #2.5
# s5 = s[-1:]
# print(s5)
#2.6
# s6 = s[-3:-8:-2]
# print(s6)
#3
# s="asdfer"
# for i in s:
#     print(i)

# aaa = 0
# while aaa < len(s):
#     print(s[aaa])
#     aaa+=1
#4
# for i in s:
#     print("asdfer")
#5
# for i in s:
#     print(i+"sb")

#6
# s = "321"
# for i in s:
#     print("倒计时"+i+"秒")
# print("出发!")

#7
# content = input("请输⼊入内容:")
# a = content.split("+")
# num1 = int(a[0])
# num2 = int(a[1])
# print(num1+num2)

#8
# content = input("请输⼊入内容:")
# a = content.split("+")
# i = 0
# sum = 0
# while i < len(a):
#     s= int(a[i])
#     i+=1
#     sum = sum + s
# print(sum)

#9
# content = input("请输⼊入内容:")
# i = 0
# total = 0
# while i < len(content):
#     s = content[i]
#     tf = (s.isdigit())
#     if tf:
#         total += 1
#     i += 1
# print(total)

#15
first_names = """ 
赵钱孙李，周吴郑王。
冯陈褚卫，蒋沈韩杨。
朱秦尤许，何吕施张。
孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。
云苏潘葛，奚范彭郎。
鲁韦昌马，苗凤花方。
俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。
滕殷罗毕，郝邬安常。
乐于时傅，皮卞齐康。
伍余元卜，顾孟平黄。
和穆萧尹，姚邵湛汪。
祁毛禹狄，米贝明臧。
计伏成戴，谈宋茅庞。
熊纪舒屈，项祝董梁。
杜阮蓝闵，席季麻强。
贾路娄危，江童颜郭。
梅盛林刁，钟徐邱骆。
高夏蔡田，樊胡凌霍。
虞万支柯，昝管卢莫。
经房裘缪，干解应宗。
丁宣贲邓，郁单杭洪。
包诸左石，崔吉钮龚。
程嵇邢滑，裴陆荣翁。
荀羊於惠，甄曲家封。
芮羿储靳，汲邴糜松。
井段富巫，乌焦巴弓。
牧隗山谷，车侯宓蓬。
全郗班仰，秋仲伊宫。
宁仇栾暴，甘钭厉戎。
祖武符刘，景詹束龙。
叶幸司韶，郜黎蓟薄。
印宿白怀，蒲邰从鄂。
索咸籍赖，卓蔺屠蒙。
池乔阴鬱，胥能苍双。
闻莘党翟，谭贡劳逄。
姬申扶堵，冉宰郦雍。
卻璩桑桂，濮牛寿通。
边扈燕冀，郏浦尚农。
温别庄晏，柴瞿阎充。
慕连茹习，宦艾鱼容。
向古易慎，戈廖庾终。
暨居衡步，都耿满弘。
匡国文寇，广禄阙东。
欧殳沃利，蔚越夔隆。
师巩厍聂，晁勾敖融。
冷訾辛阚，那简饶空。
曾毋沙乜，养鞠须丰。
巢关蒯相，查后荆红。
游竺权逯，盖益桓公。
万俟司马，上官欧阳。
夏侯诸葛，闻人东方。
赫连皇甫，尉迟公羊。
澹台公冶，宗政濮阳。
淳于单于，太叔申屠。
公孙仲孙，轩辕令狐。
钟离宇文，长孙慕容。
鲜于闾丘，司徒司空。
丌官司寇，仉督子车。
颛孙端木，巫马公西。
漆雕乐正，壤驷公良。
拓跋夹谷，宰父谷梁。
晋楚闫法，汝鄢涂钦。
段干百里，东郭南门。
呼延归海，羊舌微生。
岳帅缑亢，况郈有琴。
梁丘左丘，东门西门。
商牟佘佴，伯赏南宫。
墨哈谯笪，年爱阳佟。
第五言福，百家姓终。
"""
name = input("请输⼊您的姓名: ")
# print(name.startswith("党凯"))
# for i in first_names:
#     if name.startswith("张") == True:
#         print("百家姓中有您姓氏")
#     else:
#         print("百家姓中没有您姓氏")
fname = name[0]
print(fname)
for i in first_names:
    if first_names.find(fname) == -1:
        print("百家姓中没有您姓氏")
    else:
        print("百家姓中没有您姓氏")





































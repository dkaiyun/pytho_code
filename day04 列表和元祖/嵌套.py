lst = [['张艺谋','冯小刚','陈凯歌'],['李安','王家卫','王晶'],['周杰伦',['abc','dang_kai',['胡辣汤','c']],'柯景腾']]
print(lst)

lst[1][1] = "哈"
print(lst)

lst[2][1][1] = lst[2][1][1].replace("_","$")
print(lst)
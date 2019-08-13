tu = ("中信建投","证券","股票",tuple(),["量化平台","交易"])
print(tu)
print(tu[1])
print(tu[::2])
tu[4].append("策略")
print(tu)

for i in tu:
    print(i)
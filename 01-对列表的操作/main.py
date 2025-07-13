car = ["汽车0","汽车1","汽车2"]
#构建列表
print(car)

car.append("汽车3")
#增加列表成员
print("增加了汽车3")
print(car)

del car[0]
#使用索引删除列表成员
print("删掉了汽车0")
print(car)

car.append("汽车2")
#增加列print("删掉了汽车0")
print("增加了汽车2")
print(car)

car.insert(0,"汽车0")
#指定位置增加列表成员
print("插入了汽车0")
print(car)

car.remove("汽车2")
#删除并获取了汽车2
print("删除并获取了汽车2")
print(car)

car.sort()
print("排序了汽车")
print(car)

car.reverse()
print("排序了汽车")
print(car)

print(len(car))
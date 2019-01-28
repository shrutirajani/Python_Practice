lst = [1]
print(1,1,1)
for j in range(100):
    val = -1
    count = -1
    newlst = []
    for i,item in enumerate(lst):
        if i==0:
            val = item
            count = 1
            continue
        if item == val:
            count += 1
        else:
            newlst.append(count)
            newlst.append(val)
            val = item
            count = 1
    newlst.append(count)
    newlst.append(val)
    print(j+2,max(newlst),len(newlst))
    lst = newlst

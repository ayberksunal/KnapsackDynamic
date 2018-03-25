
# instructor: Elena Battini Sonmez / Mujde Aktas

def knapsack(items,weightback):
    if items ==[]: # is list is empty
        return([],0);
    elif items[0][1]> weightback: #to control the size of the backpack
        return knapsack(items[1:],weightback)
    else:
        #knapsack(rest,cap)
        list1,val1 = knapsack(items[1:],weightback) #send to the function with the rest of the list
        #knapsack(list,cap-item)
        list2,val2 = knapsack(items[1:],weightback - items[0][1]) #send to the function with the rest of the list(wieght-itemweigh)
        # v1>v2 + loi[0]
        if val1 > val2 + items[0][2]:
            #do not take
            return (list1,val2)
        else:
            #take
            return(list2 + [items[0][0]], val2 + items[0][2])

itemslist = [('banana', 1, 1), ('jewelery', 3, 4), ('book', 4, 5), ('keys', 5, 7)]
#name,size,value => an item of the list
#second var of the function= size of the backpack

print knapsack(itemslist,7)  # (['jewelery', 'book'], 4)
print knapsack(itemslist,10)  #(['banana', 'book', 'keys'], 1)
print knapsack(itemslist,30)  #(['banana', 'jewelery', 'book', 'keys'], 17)
print knapsack(itemslist,3)   #(['jewelery'], 0)




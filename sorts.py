import math

test = [0,3,2,4,7,5,9,1]

def bubble_sort(list:list,i):
    for i in range(i, 0, -1):
        for j in range(0, i-1):
            if(list[j]>list[j+1]):
                list[j], list[j+1]=list[j+1],list[j]
            print(f"{i}: {list}")
    return list
def insertion_sort(list:list):
    pass

bubres = bubble_sort(test, len(test))
print(bubres)
import time
list1=[0,1]
while(True):
    n=len(list1)
    list1.append(list1[n-1]+list1[n-2])
    print(list1)
    time.sleep(2)
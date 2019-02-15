mylist = [10,50,45,22,36,78]
q = 36
for ele in mylist:
    if q == ele:
        print("query element found")
        break
else:
    print("query element not found")

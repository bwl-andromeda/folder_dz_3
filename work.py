def open_dict():
    list_1 = ["1.txt","2.txt","3.txt"]
    basic_dict = {}
    for i in list_1:
        with open(i,encoding="UTF-8") as f:
            a = f.readlines()
            basic_dict[i] = len(a)
            sorted_files = sorted(basic_dict.items(),key=lambda item: item[1])
    for keys,values in sorted_files:
        i = 0
        print(keys)
        print(values)
        for line in open(keys,encoding="UTF-8"):
            i+=1
            print(line,end = "")
        print("\n",end = "")
    
        
open_dict()







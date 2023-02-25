def open_dict(name):
    d = open("result.txt","w",encoding="UTF-8")
    basic_dict = {}
    for i in name:
        with open(i,encoding="UTF-8") as f:
            a = f.readlines()
            basic_dict[i] = len(a)
            sorted_files = sorted(basic_dict.items(),key=lambda item: item[1])
    for keys,values in sorted_files:
        d.writelines(f'{keys}\n')
        d.writelines(f'{str(values)}\n')
        for line in open(keys,encoding="UTF-8"):
            d.writelines(line)
        d.writelines("\n")



list_1 = ["1.txt","2.txt","3.txt"]        
open_dict(list_1)







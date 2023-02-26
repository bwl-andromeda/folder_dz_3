def open_dict(name):
    with open("result.txt","w",encoding="UTF-8") as d:
        basic_dict = {}
        for i in name:
            with open(i,encoding="UTF-8") as f: a = f.readlines()
            basic_dict[i] = len(a)
        for keys,values in sorted(basic_dict.items(),key=lambda item: item[1]):
            d.writelines(f'{keys}\n{str(values)}\n')
            for line in open(keys,encoding="UTF-8"): d.writelines(line)
            d.writelines("\n")



list_1 = ["1.txt","2.txt","3.txt"]        
open_dict(list_1)







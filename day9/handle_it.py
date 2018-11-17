# -*- coding: utf-8 -*-

# '''
# # <a class="s xst" href="https://www.kxdao.net/forum.php?mod=viewthread&tid=186373&extra=page%3D1" onclick="atarget(this)"
# # '''
result_list = []
with open("1.txt","r",encoding='utf-8') as f:
    for line in f.readlines():
        lines=line.split('"')
        kk=lines[6].strip(">")
        # print(kk)
        zz=kk.replace('</a>','')
        result_list.append(lines[3]+'  '+zz)

result_list.remove(result_list[0])
result_list.remove(result_list[0])
result_list.remove(result_list[0])
with open("new.txt","w",encoding="utf-8") as f:
    for i in result_list:
        if i :
            f.write(i)
        else:
            f.close()







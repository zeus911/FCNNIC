"""
连续IP段整理成a.b.c.0-a.b.c.255的格式.py
http://bbs.bathome.net/thread-31568-1-1.html
2016年3月3日 02:15:42 codegay
"""
import pprint
#生成测试文件
open("3.txt","w+").write("""9.79.12.0 
9.79.116.0
9.79.219.0
9.79.221.0
9.79.222.0
149.80.1.0
149.80.42.0
149.80.144.0
149.80.249.0
119.189.73.0
119.189.74.0
119.189.82.0
119.189.84.0
119.189.96.0
119.189.99.0
119.189.84.0
119.189.96.0
119.189.199.0
119.189.255.0""")

txt=open("3.txt").readlines()
abc=[r.split(".")[:-1] for r in txt]
ab=sorted(list({r[0]+'.'+r[1] for r in abc}))
for a in ab:
    ccc=['.'.join(r.split(".")[:-1]) for r in txt if a+"." in r]
    print('整理结果',min(ccc)+'.0'+'-'+max(ccc)+'.255')

"""
输出:
整理结果 119.189.199.0-119.189.99.255
整理结果 9.79.116.0-9.79.222.255
整理结果 149.80.1.0-149.80.42.255
"""

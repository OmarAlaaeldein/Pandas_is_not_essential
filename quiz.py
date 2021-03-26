from datetime import datetime
diff_list=[]
import matplotlib.pyplot as plt
l=[]
date=[]
time=[]
with open(r"C:\Users\omara\PycharmProjects\pythonProject\outputfile.txt", 'r') as file:
    data = file.readlines()
for i in data:
    
    print(i)
    l.append(i.split(',')[2:-1])
    date.append((i.split(',')[0]))
    time.append((i.split(',')[1].split(':')[0:3]))
since=datetime(int(date[0].split('/')[2]),int(date[0].split('/')[0]),int(date[0].split('/')[1]),int(time[0][0]),int(time[0][1]),int(time[0][2]))
for i in range(len(time)):
    diff_list.append((datetime(int(date[i].split('/')[2]),int(date[i].split('/')[0]),int(date[i].split('/')[1]),int(time[i][0]),int(time[i][1]),int(time[i][2]))-since).total_seconds())

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]=int(l[i][j],16)
def dic(j):
    r=[]
    mylist=['yoc_temp','yoc_SP','yoc_p1','yoc_p2','yoc_p3','yoc_p4','yoc_p5','yoc_bl1','yoc_bl2','yoc_lights','yoc_stereo','yoc_h1','yoc_h2','yoc_filter']
    for i in range(len(l)):
        r.append(l[i][mylist.index(j)])
    return r
fig, ax=plt.subplots(3)
ax0twinx=ax[0].twinx()
ax[0].plot(diff_list,dic('yoc_temp'),label='yoc_temp',color='red')
ax[0].plot(diff_list,dic('yoc_SP'),label='yoc_SP',color='blue')
ax0twinx.plot(diff_list,dic('yoc_p1'),label='yoc_p1',color='green')
ax0twinx.legend()
ax[0].legend()
plt.show()
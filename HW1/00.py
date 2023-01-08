from asyncio.windows_events import NULL


save=NULL
for i in range(0,100):
    if (i>save):
        save=i
print(save)

a=[0,1,2]
a.pop()
print(a)
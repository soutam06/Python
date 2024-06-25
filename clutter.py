import os
# n=0
# files=os.listdir('pngs')
# for file in files:
#     if file.endswith(".png"):
#         n=n+1
#         # print(file)
#         os.rename(f"pngs/{file}",f"pngs/{n}.png")
# os.remove('pngs/1.png')
for i in range(9):
    os.removedirs(f"pngs/file{i}.txt")
    

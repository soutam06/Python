import time

def local_time():
    t=time.localtime()
    formatted_time=time.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time)

local_time()
time.sleep(10)      #To stop the time for 10 Secoends
local_time()
print("This line is exicuted after 10 secoends")
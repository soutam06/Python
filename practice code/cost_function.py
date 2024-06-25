import inspect, os
path = os.path.abspath(inspect.getfile(plt_stationary))
# print(path)
f = open(path, 'r')
content = f.read()
print(content)
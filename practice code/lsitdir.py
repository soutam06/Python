import os
files=[file for file in os.listdir() if file.endswith('.exe') or file.endswith('.c')]

for file in files:
    os.remove(file)
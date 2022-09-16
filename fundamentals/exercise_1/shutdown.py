import os

shutdown = input("Shutdown your PC? (yes/no)")

if shutdown == "no":
    exit()
else:
    os.system("shutdown /s /t 1")

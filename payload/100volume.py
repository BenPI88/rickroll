import os
while True:
    os.system("amixer sset Master 100%")
    os.system("amixer sset Master unmute")
    os.system("amixer sset Headphone 100%")
    os.system("amixer sset Headphone unmute")

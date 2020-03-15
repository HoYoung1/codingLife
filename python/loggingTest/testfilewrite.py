import time

while True:
    with open('testhy.txt','a') as f:
        f.write(time.strftime('%c', time.localtime(time.time()))+"\n")
    time.sleep(60)


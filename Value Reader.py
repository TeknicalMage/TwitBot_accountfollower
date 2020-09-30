import time

f = open("values.txt", "r")

line = f.readline()

y = open('actual.txt', 'a')

cnt = 1
while line:
    x = (line.strip())
    #print(x)
    line = f.readline()
    cnt += 1

    z = str(x)

    if ("@") in z:
        print(z)
        y.write(z +"\n")
    else:
        time.sleep(0)


    #print(z)
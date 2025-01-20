import time

initial = time.time()
i = 1
while (i<=100):
    print("Hello while loop Shan")
    i = i+1
print(f"While Loop initial time was {initial} and end time is {time.time()}\n")

for j in range(100):
    print('Hello for loop Shan')
    # time.sleep(0.5)
print(f"for Loop initial time was {initial} and end time is {time.time()}\n")


# current time

currentTime = time.asctime(time.localtime(time.time()))
print("Current Time")
print(currentTime)
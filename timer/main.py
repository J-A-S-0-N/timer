from time import sleep
from os import system

# def main(time):
#     for i in range(0,time):
#         print(time)
#         time -= 1
#         sleep(1)
#         system("cls")
#         if time == 0:
#             print("time ended")
#             break

# if __name__ == "__main__":
#     print("enter the time")
#     inp = input(">>")
#     main(int(inp))
print("enter the time")
time = input(">>")
time = int(time)

for i in range(0,time):
    print(time)
    time -= 1
    sleep(1)
    system("cls")
    # if time == 0:
    #     print("time ended")

# if __name__ == "__main__":
#     print("enter the time")
#     inp = input(">>")
#     main(int(inp))
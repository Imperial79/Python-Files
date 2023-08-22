

n = 7

# for i in range(n):
#     for j in range(n):
#         if (i <= int(n/2) and (i+j <= int(n/2) or j-i >= int(n/2))) or (i >= int(n/2) and (i-j >= int(n/2) or i+j >= (int(n/2) + (n-1)))):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

for i in range(n):
    for j in range(n):
        if (j <= int(n/2) and i <= int(n/2) and i+j >= int(n/2)) or (j >= int(n/2) and i >= int(n/2) and i+j <= int(n/2) + (n-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

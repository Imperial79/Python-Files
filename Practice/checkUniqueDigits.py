count = 0
m = int(input('Enter start limit: '))
n = int(input('Enter end limit: '))

if (m > n):
    print('Start limit must me less than end limit !!')

else:
    for i in range(m, n):
        if (i < 10):
            count += 1
            print(i)
        else:
            temp = i
            arr = []
            flag = 0
            while (temp != 0):
                rem = temp % 10
                if str(i).count(str(rem)) > 1:
                    # arr.append(rem)
                    # else:
                    flag = 1
                    break
                temp /= 10
            if flag != 1:
                count += 1
                print(i)

    print("No. of unique integers: ", count)

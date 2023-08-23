# 5. CheckPassword(char str[]);
# The function accepts string str. Implement the function which returns 1 if given string str
# is valid password else 0.
# str is a valid password if it satisfies the below conditions.
# – At least 6 characters
# – At least one numeric digit
# – At least one capital Letter
# – At least one small Letter
# – At least one special character($ , # %,@ )
# – Must not have space or slash (/)
# – Starting character must not be a number


def checkPassword(password):
    if (len(password) >= 6):
        if (password[0].isdigit()):
            return 0
        d = s = l = c = 0
        for i in password:
            if (i.__contains__(' ') or i.__contains__('/')):
                return 0
            elif (i.isdigit()):
                d += 1
            elif (i.islower()):
                l += 1
            elif (i.isupper()):
                c += 1
            elif (i in '$#%@'):
                s += 1

            if (d > 0 and l > 0 and s > 0 and c > 0):
                return 1

    else:
        return 0


print(checkPassword("Warrior889"))
# i = "Warrior/889"
# print(i.__contains__(' ') or i.__contains__('/'))
# a = 'abc'

# print(a.__contains__('a'))
# a[1].isupper()
# a[1].isdigit()

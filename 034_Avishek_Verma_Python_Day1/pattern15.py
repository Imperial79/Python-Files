'''
* * * * *       *
  * * * *     * *
    * * *   * * *
      * * * * * *
* * * * * * * * *
* * * * * *
* * *   * * *
* *     * * * *
*       * * * * *
'''

n = int(input("Enter rows: "))

for i in range(n):
    for j in range(n):
        if ((i <= j and j <= int(n/2)) or
            (i+j >= (n-1) and j <= (n-1) and i <= int(n/2)) or
                (i >= int(n/2) and i >= j and i+j <= (n-1)) or
                j >= int(n/2) and i-j >= 0):
            print("* ", end='')
        else:
            print("  ", end="")
    print()

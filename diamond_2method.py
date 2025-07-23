rows = int(input("Rows enter karo (odd number): "))
mid = rows // 2 + 1  
for i in range(1, rows + 1):
    if i <= mid:
        stars = 2 * i - 1
        spaces = mid - i
    else:
        stars = 2 * (rows - i) + 1
        spaces = i - mid
    print(" " * spaces + "*" * stars)

list = [1, 2, 4, 7, 6, 0, 1, 2]

print(list[:3])
mid_number=int(len(list)/2)
print(mid_number)

if mid_number%2==0:
    print(list[mid_number-1]) #sudy pocet cisel, rvni z dvojice "print(list[mid_number])" druhe z dvojice
else:
    print(list[mid_number]) #lichy pocet cisel

    
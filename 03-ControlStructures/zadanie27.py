# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f' {i+j}',end='')
#     print()

liczba = 6
while liczba >= 0:
    pomocniczaLiczba = 1
    while pomocniczaLiczba <= 3:
        if pomocniczaLiczba == 3:
            print(liczba + pomocniczaLiczba)
        else:
            print(liczba + pomocniczaLiczba,end=" ")
        pomocniczaLiczba = pomocniczaLiczba+1
    liczba = liczba - 3
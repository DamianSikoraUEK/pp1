def display_integers(N):
    integers = ""
    for i in range(1,N+1):
        if i == 1:
            integers = str(i) + " "
        else: integers = integers + str(i) + " "
    return integers
print("liczby całkowite od 1 do 15 to: " + display_integers(15))
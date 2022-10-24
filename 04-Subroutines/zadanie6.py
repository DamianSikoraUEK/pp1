def keypad():
    klawiatura = ""
    for i in range(1,10):
        if i == 1:
            klawiatura = str(i) + " "
        elif i == 9:
            klawiatura = klawiatura + str(i)
        elif i % 3 == 0:
            klawiatura = klawiatura + str(i) + "\n"
        else:
            klawiatura = klawiatura +str(i) +" "
    return klawiatura
print(keypad())

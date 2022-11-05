def month(n):
    if n > 12 or n < 1:
        return "Brak takiego miesiąca"
    for i in range(1,len(months)+1):
        if i == n-1:
            return months[i]

months = ('styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień')
miesiac = 6
print(f"{miesiac} miesiąc to {month(miesiac)}")


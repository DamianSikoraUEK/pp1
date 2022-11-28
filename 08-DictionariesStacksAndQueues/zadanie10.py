countries = [{"name": "Poland","population":"38mln"},
{"name": "Germany","population":"83mln"},
{"name": "France","population":"68mln"},
{"name": "Spain","population":"47mln"},
{"name": "Denmark","population":"6mln"}]
i = 0
while i < len(countries):
    for key,value in countries[i].items():
        print(value,end=":")
    print("")
    i = i+1
c = 0  # dichiara c come variabile globale

def f(x):
    global c  # dichiara c come variabile globale

    if x <= 0:
        return x
    else:
        c += 1
        return f(x-1) - f(x-2)

total_calls = f(20)
print("Numero totale di chiamate:",c)

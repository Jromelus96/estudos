def meu_function(a):
    c = float(input("informe a temperatura °C: "))
    f = ((c * 9) / 5) + 32
    print(" A temperatura de {}°C corresponde a {}°F!".format(c,f))
    print(a)
meu_function("argumento")

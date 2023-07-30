import matplotlib.pyplot as plt


def collatz(numero):
    resultados = []
    while True:
        if numero == 1 or numero == 0:
            print(numero)
            return resultados
        if numero % 2 != 0:
            numero = (numero*3)+1
            resultados.append(numero)
        else:
            numero = numero/2
            resultados.append(numero)

plt.figure(figsize=(8, 6))
plt.yticks(range(100))
plt.ylabel("Valor")
plt.title("Secuencias de Collatz")

for i in range(1000):
    resultado = collatz(i)
    print(f"Secuencia para el número {i}: {resultado}")
    plt.plot(resultado, marker='o', linestyle='-')

plt.grid(True)
plt.tight_layout()

plt.show()
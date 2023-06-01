import numpy as np
import matplotlib.pyplot as plt

# Función para trazar un gráfico de línea
def plot_line(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de Línea')
    plt.show()

# Función para trazar un gráfico de dispersión
def plot_scatter(x, y):
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de Dispersión')
    plt.show()


# Función para trazar un gráfico de barras
def plot_bar(x, y):
    plt.bar(x, y)
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Gráfico de Barras')
    plt.show()

# Función para trazar un gráfico de torta
def plot_pie(labels, sizes):
    explode = [0.1] * len(labels)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Gráfico de Torta')
    plt.show()


def main():
    print("Bienvenido a la Demostración Interactiva de Matplotlib!")
    while True:
        print("1. Gráfico de Línea")
        print("2. Gráfico de Dispersión")
        print("3. Gráfico de Barras")
        print("4. Gráfico de Torta")
        print("5. Salir")
        choice = input("Ingrese el número correspondiente a la función que desea visualizar (o 5 para salir): ")

        if choice == '1':
            # Se solicitan los valores de x e y al usuario
            x = input("Ingrese los valores de x (separados por comas): ")
            y = input("Ingrese los valores de y (separados por comas): ")
            # Los valores de x e y se convierten en arrays de NumPy con el tipo de datos float
            x = np.array(x.split(','), dtype=float)
            y = np.array(y.split(','), dtype=float)
            # Se llama a la función plot_line para trazar el gráfico de línea
            plot_line(x, y)
        elif choice == '2':
            # Se solicitan los valores de x e y al usuario
            x = input("Ingrese los valores de x (separados por comas): ")
            y = input("Ingrese los valores de y (separados por comas): ")
            # Los valores de x e y se convierten en arrays de NumPy con el tipo de datos float
            x = np.array(x.split(','), dtype=float)
            y = np.array(y.split(','), dtype=float)
            # Se llama a la función plot_scatter para trazar el gráfico de dispersión
            plot_scatter(x, y)
        elif choice == '3':
             # Se solicitan las categorías y los valores al usuario 
            x = input("Ingrese las categorías (separadas por comas): ")
            y = input("Ingrese los valores (separados por comas): ")
            # Las categorías se mantienen como strings y los valores se convierten en un array de NumPy con el tipo de datos float
            x = np.array(x.split(','), dtype=str)
            y = np.array(y.split(','), dtype=float)
            # Se llama a la función plot_bar para trazar el gráfico de barras
            plot_bar(x, y)
        elif choice == '4':
            # Se solicitan las etiquetas y los tamaños al usuario
            labels = input("Ingrese las etiquetas (separadas por comas): ")
            sizes = input("Ingrese los tamaños (separados por comas): ")
            # Las etiquetas se mantienen como una lista y los tamaños se convierten en un array de NumPy con el tipo de datos float
            labels = labels.split(',')  
            sizes = np.array(sizes.split(','), dtype=float)
            # Se llama a la función plot_pie para trazar el gráfico de torta
            plot_pie(labels, sizes)
        elif choice == '5':
            # Si se selecciona '5', se sale del bucle y se termina el programa
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del 1 al 5.")

        answer = input("¿Desea realizar otra operación? (Sí/No): ")
        if answer.lower() != 'sí' and answer.lower() != 'si':
            break

if __name__ == "__main__":
    main()

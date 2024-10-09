import random
import tkinter as tk
from cProfile import label
from doctest import master
from tkinter import NE, ttk

from PIL import ImageTk, Image
def show_result(result):
    if result == 'victoria':
        print("¡Felicidades, ganaste!")
    elif result == 'derrota':
        print("Lo siento, has perdido.")
    elif result == 'empate':
        print("¡Es un empate!")

def menu():
    root = tk.Tk()
    root.title("Menú de juegos")
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    root.geometry("600x600")

    img = Image.open("images/imagen_menu_principal.png").resize((600, 600))
    filename_menu = ImageTk.PhotoImage(img)


    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(10, 10, image=filename_menu, anchor="nw")
    canvas.create_text(270, 60, fill="black", font="calibri 30")

    button_game1 = ttk.Button(root, text="Piedra Papel Tijera", command=rock_paper_scissor)
    button_game2 = ttk.Button(root, text="Adivina el número", command=guess_number)
    button_game3 = ttk.Button(root, text="Traducir", command=translator)
    quit_button = ttk.Button(root, text="Salir", command=root.destroy)

    canvas.create_window(250, 200, anchor="nw", window=button_game1)
    canvas.create_window(250, 300, anchor="nw", window=button_game2)
    canvas.create_window(250, 400, anchor="nw", window=button_game3)
    canvas.create_window(250, 500, anchor="nw", window=quit_button)



    root.mainloop()

def rock_paper_scissor():
    label = ttk.Label(rock_paper_scissor())

def guess_number():
    pass

def translator():
    number = random.randint(0, 200)
    intentos = 5

    for intento in range(1, intentos + 1):
        try:
            player = int(input(f"Intento {intento}/{intentos}. Adivina el número (0-200): "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if player == number:
            return 'victoria'
        elif player < number:
            print("El número es mayor.")
        else:
            print("El número es menor.")

    print(f"El número era {number}.")
    return 'derrota'

menu()
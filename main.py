import tkinter as tk
import random

escolha_usuario = None

def escolher_cara():
    global escolha_usuario
    escolha_usuario = "cara"
    label_escolha.config(
        text="Você escolheu cara"
    )
    botao_moeda.pack()
    print("Cara escolhida")

def escolher_coroa():
    global escolha_usuario
    escolha_usuario = "coroa"
    label_escolha.config(
        text="Você escolheu coroa"
    )
    botao_moeda.pack()
    print("Coroa escolhida")

def girar_moeda():
    print("Girando...")
    resultado = random.choice(
    ["cara","coroa"]
)

    print(resultado)
    
    if resultado == escolha_usuario:
        mensagem = f"Você ganhou! Saiu {resultado.upper()}"
        cor = "green"
    else:
        mensagem = f"Você perdeu! Saiu {resultado.upper()}"
        cor = "red"
    
    label_resultado.config(
        text=mensagem,
        fg=cor,
        font=("Arial", 14, "bold")
    )


root = tk.Tk()
root.title('Cara ou Coroa')
root.geometry('600x400')


label_titulo = tk.Label(
    root,
    text='Escolha entre Cara ou Coroa',
    bg='grey',
    fg='white',
    font=("Arial", 14, "bold")
)

label_titulo.pack(pady=20)

frame_botoes = tk.Frame(root)
frame_botoes.pack()

botao_cara = tk.Button(
    frame_botoes,
    text='Cara',
    command=escolher_cara,
    font=("Arial", 14, "bold"),
    width=10
    )

botao_cara.pack(
    side='left',
    padx=20,
    pady=30
    ) 

botao_coroa = tk.Button(
    frame_botoes,
    text='Coroa',
    command=escolher_coroa,
    font=("Arial", 14, "bold"),
    width=10
    )

botao_coroa.pack(
    side='right',
    padx=20,
    pady=30
    )

label_escolha = tk.Label(
    root,
    text="Nenhuma escolha feita"
)

label_escolha.pack()

botao_moeda = tk.Button(
    root,
    text="Gire a moeda",
    command=girar_moeda,
    font=("Arial", 14, "bold"),
    width=15,
    pady=10
)

botao_moeda.pack(pady=20)

label_resultado = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    fg="black",
    pady=20
)

label_resultado.pack()


root.mainloop()


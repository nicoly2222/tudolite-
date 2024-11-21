import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg="#2e305e")
janela.geometry("500x600")

frame_em_edicao = None

def adicionar_tarefa():
    global frame_em_edicao
    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, insira uma tarefa válida")


def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior,bg="white", bd = 1, relief =  tk.SOLID)
    
    label_tarefa = tk.Label(frame_tarefa, text = tarefa,font=("Garamond,16"), bg = "white", width = 25, anchor= "w")
    label_tarefa.pack(side = tk.LEFT, fill = tk.X,padx = 10,pady = 5)
    
    botao_editar = tk.Button(frame_tarefa, image= icon_editar, command= lambda f = frame_tarefa, l = label_tarefa: preparar_edicao(f,1) ,bg= "white",relief = tk.FLAT )
    botao_editar.pack(side = tk.RIGHT , padx = 5 )
    
    botao_deletar = tk.Button(frame_tarefa, image= icon_deletar, command= lambda f = frame_tarefa, l = label_tarefa: deletar_tarefa(f), bg= "white",relief = tk.FLAT )
    botao_deletar.pack(side = tk.RIGHT , padx = 5 )
    
    frame_tarefa.pack(fill = tk.X, padx = 5, pady = 5)
    
    checkbutton = ttk.Checkbutton(frame_tarefa, command = lambda label = label_tarefa: alternar_sublinhado(label))
    checkbutton.pack(side = tk.RIGHT ,padx = 5 )
    
    canvas_interior.update_idlestaks()
    canvas.config(scrollregion = canvas.bbox("all"))
    
def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao 
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0,tk.END)
    entrada_tarefa.insert(0,label_tarefa.cget("text"))
    
def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text = nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion = canvas.bbox("all"))
    
def alternar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace("overstrike","")
    else:
        nova_fonte = fonte_atual + "overstrike"
    label.config(font=nova_fonte)

def ao_clicar_entrada(event):
    if entrada_tarefa.get() == "Escreva sua tarefa aqui":
        entrada_tarefa.delete(0,tk.END)
        entrada_tarefa.configure(fg="black")

def ao_sair_foco(event):
    if not entrada_tarefa.get().strip():
        entrada_tarefa.delete(0,tk.END)
        entrada_tarefa.insert(0,"Escreva sua tarefa aqui")
        entrada_tarefa.configure(fg = "grey")

icon_editar = PhotoImage(file="edit.png").subsample(4,4)
icon_deletar = PhotoImage(file="delete.png").subsample(4,4)



fonte_cabecalho = font.Font(family = "Garamond", size = 24 , weight= "bold")


rotulo_cabecalho = tk.Label(janela, text = "Meu app de trabalho", font = fonte_cabecalho, bg ="#2e305e", fg ="#C0C0C0")
rotulo_cabecalho.pack(pady =20)

frame = tk.Frame(janela, bg ="#2e305e")
frame.pack(pady= 10)

entrada_tarefa = tk.Entry(frame, font = ("Garamond", 14), relief = tk.FLAT, bg ="white", fg = "grey", width = 30 )
entrada_tarefa.insert(0,"Escreva sua tarefa aqui")
entrada_tarefa.bind("<FocusIn>",ao_clicar_entrada)
entrada_tarefa.bind("FocusOut",ao_sair_foco)
entrada_tarefa.pack(side = tk.LEFT,padx = 10)

botao_adicionar = tk.Button(frame, text= "Adicionar Tarefa", command = adicionar_tarefa, bg = "#4C4F50", fg = "white", height = 1, width = 15, font = ("Roboto",11), relief = tk.FLAT )
botao_adicionar.pack(side = tk.LEFT , padx = 10 )

frame_lista_tafefas = tk.Frame(janela, bg = "#C0C0C0")
frame_lista_tafefas.pack(fill = tk.BOTH, expand = True, padx = 10 , pady = 10)
canvas = tk.Canvas(frame_lista_tafefas, bg ="#C0C0C0")
canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
scrollbar = ttk.Scrollbar(frame_lista_tafefas,orient = "vertical")
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

canvas.configure(yscrollcommand= scrollbar.set)
canvas_interior = tk.Frame(canvas,bg = "#C0C0C0")
canvas.create_window((0,0), window = canvas_interior, anchor = "nw")
canvas.configure(scrollregion=canvas.bbox("all"))

janela.mainloop()
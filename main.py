import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import webbrowser 
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Configuração do Google Sheets
def configurar_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_891ySuN0cHCcw-brOIYgsaq7TRJo8aGiSVSXD3b3eM/edit#gid=0").sheet1
    return sheet

try:
    sheet = configurar_google_sheets()
    print("Conexão com o Google Sheets realizada com sucesso!")
except Exception as e:
    print("Erro ao conectar com o Google Sheets:", e)


def adicionar_valor_celulas(sheet, data, campanha, status):
    nova_linha = [data, campanha, status]
    sheet.append_row(nova_linha)


def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


def enviar_dados():
    data = entry_data.get()
    campanha = entry_campanha.get()
    status = entry_status.get()

    if not data or not campanha or not status:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    try:
        adicionar_valor_celulas(sheet, data, campanha, status)
        messagebox.showinfo("Sucesso", "Os dados foram enviados com sucesso!")
        entry_data.delete(0, tk.END)
        entry_campanha.delete(0, tk.END)
        entry_status.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar dados: {e}")


def abrir_planilha():
    url_planilha = "https://docs.google.com/spreadsheets/d/1_891ySuN0cHCcw-brOIYgsaq7TRJo8aGiSVSXD3b3eM/edit#gid=0"
    webbrowser.open(url_planilha)


# Inicializa a janela principal
janela = tk.Tk()
janela.title("Formulário de Entrada de Dados")

# Define o tamanho desejado da janela e centraliza
largura_janela = 400
altura_janela = 350
centralizar_janela(janela, largura_janela, altura_janela)

# Widgets do formulário
label_data = ttk.Label(janela, text="Data (DD/MM/AAAA):")
label_data.pack(pady=5)
entry_data = ttk.Entry(janela)
entry_data.pack(pady=5)

label_campanha = ttk.Label(janela, text="Nome da Campanha:")
label_campanha.pack(pady=5)
entry_campanha = ttk.Entry(janela)
entry_campanha.pack(pady=5)

label_status = ttk.Label(janela, text="Status do Print:")
label_status.pack(pady=5)
entry_status = ttk.Entry(janela)
entry_status.pack(pady=5)

# Botão para enviar os dados
botao_enviar = ttk.Button(janela, text="Enviar", command=enviar_dados)
botao_enviar.pack(pady=10)

# Botão para abrir a planilha no navegador
botao_abrir_planilha = ttk.Button(janela, text="Abrir Planilha", command=abrir_planilha)
botao_abrir_planilha.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()
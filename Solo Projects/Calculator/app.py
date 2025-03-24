from flask import Flask, render_template, request, jsonify
import threading
import tkinter as tk
from tkinter import ttk
import webview

app = Flask(__name__)

# Rota principal para renderizar a calculadora
@app.route('/')
def home():
    return render_template('index.html')

# Rota para cálculos
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression')
    try:
        result = eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Função para rodar o Flask em segundo plano
def run_flask():
    app.run(port=5000)

# Função para criar a janela do aplicativo
def create_app_window():
    window = tk.Tk()
    window.title("Calculadora Moderna")
    window.geometry("400x600")

    # Cria um frame para o conteúdo
    frame = ttk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Usa a biblioteca `webview` para carregar o Flask no Tkinter
    webview.create_window("Calculadora", "http://127.0.0.1:5000", width=400, height=600)
    webview.start()

    window.mainloop()

if __name__ == '__main__':
    # Inicia o Flask em uma thread separada
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Cria a janela do aplicativo
    create_app_window()
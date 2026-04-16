from flask import Flask, request, render_template, redirect
import datetime

app = Flask(__name__)

# Simulação de Banco de Dados
agendamentos = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    # Coleta de dados do formulário
    nome = request.form.get('nome')
    whatsapp = request.form.get('whatsapp')
    servico = request.form.get('servico')
    data_hora = request.form.get('data_hora')

    # Cria o registro do agendamento
    novo_agendamento = {
        "cliente": nome,
        "contato": whatsapp,
        "servico": servico,
        "horario": data_hora,
        "status": "pendente"
    }

    agendamentos.append(novo_agendamento)
    
    # Aqui você pode integrar a API do WhatsApp para enviar confirmação
    print(f"Novo Agendamento: {nome} - {servico} às {data_hora}")

    return "<h2>Agendamento realizado com sucesso! Em breve entraremos em contato.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
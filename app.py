from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Respostas simuladas para teste
MOCK_RESPONSES = [
    "Olá! Como posso te ajudar hoje?",
    "Interessante pergunta! Deixe-me pensar...",
    "Entendo seu ponto. Aqui está minha resposta:",
    "Ótima questão! Vou explicar melhor:",
    "Posso te ajudar com isso. Veja:",
    "Claro! Aqui está uma explicação:",
]

@app.route("/")
def home():
    return render_template('chat.html')

@app.route("/chat", methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mensagem vazia'}), 400
        
        # Simulação de resposta (para teste)
        mock_response = random.choice(MOCK_RESPONSES)
        ai_response = f"{mock_response} Você disse: '{user_message}'"
        
        return jsonify({'response': ai_response})
        
    except Exception as e:
        return jsonify({'error': f'Erro: {str(e)}'}), 500

@app.route("/status")
def status():
    return jsonify({
        'status': 'online', 
        'models': ['mock-gemma'],
        'message': 'Modo de teste - Ollama será adicionado em breve'
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Configuração do Ollama (conecta ao Ollama da VPS)
OLLAMA_URL = "http://localhost:11434"

@app.route("/")
def home():
    return render_template('chat.html')

@app.route("/chat", methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mensagem vazia'}), 400
        
        # Chamada para o Ollama com Gemma
        payload = {
            "model": "gemma:2b",
            "prompt": user_message,
            "stream": False
        }
        
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            ai_response = result.get('response', 'Erro na resposta')
            return jsonify({'response': ai_response})
        else:
            return jsonify({'error': f'Ollama retornou status {response.status_code}'}), 500
        
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Não foi possível conectar ao Ollama. Verifique se está rodando na porta 11434.'}), 500
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout na resposta do Ollama. Tente novamente.'}), 500
    except Exception as e:
        return jsonify({'error': f'Erro: {str(e)}'}), 500

@app.route("/status")
def status():
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            return jsonify({'status': 'online', 'models': models})
        else:
            return jsonify({'status': 'offline', 'error': f'Status {response.status_code}'}), 500
    except requests.exceptions.ConnectionError:
        return jsonify({'status': 'offline', 'error': 'Conexão recusada'}), 500
    except Exception as e:
        return jsonify({'status': 'offline', 'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
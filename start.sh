#!/bin/bash

# Iniciar Ollama em background
ollama serve &

# Aguardar Ollama inicializar
sleep 10

# Baixar modelo Gemma se não existir
ollama pull gemma:2b

# Iniciar aplicação Flask
python app.py
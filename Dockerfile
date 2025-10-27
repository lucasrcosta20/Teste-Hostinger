FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copiar arquivos da aplicação
COPY app.py .
COPY templates/ templates/

# Instalar dependências Python
RUN pip install flask requests

# Expor portas
EXPOSE 8000
EXPOSE 11434

# Script de inicialização
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
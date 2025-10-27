FROM python:3.11-slim

WORKDIR /app

# Copiar arquivos da aplicação
COPY app.py .
COPY templates/ templates/

# Instalar dependências Python
RUN pip install flask

# Expor porta
EXPOSE 8000

# Iniciar aplicação
CMD ["python", "app.py"]
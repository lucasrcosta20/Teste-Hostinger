# Chat com Gemma - Ollama

Aplicação de chat completa usando Flask + Ollama + Gemma rodando em Docker.

## 🚀 Funcionalidades

- Chat em tempo real com modelo Gemma
- Interface web moderna e responsiva
- Ollama rodando localmente no container
- Status indicator do modelo
- Deploy automatizado com Docker

## 🛠️ Quick Start

```bash
# Clone o repositório
git clone https://github.com/lucasrcosta20/Teste-Hostinger.git
cd Teste-Hostinger

# Build e run com Docker Compose
docker compose up -d --build
```

## 🌐 Acesso

- **Local**: http://localhost:8080
- **VPS**: http://72.61.219.206:8080
- **Hostname**: http://srv1087217.hstgr.cloud:8080

## 📁 Estrutura

- `app.py` - Aplicação Flask com endpoints do chat
- `templates/chat.html` - Interface web do chat
- `Dockerfile` - Container com Ollama + Flask
- `docker-compose.yml` - Orquestração dos serviços
- `start.sh` - Script de inicialização

## ⚙️ Como Funciona

1. Container inicia Ollama em background
2. Download automático do modelo Gemma 2B
3. Flask serve a interface web
4. Chat se conecta via API REST ao Ollama

## 🔧 Deploy na VPS

```bash
# Na VPS
git clone https://github.com/lucasrcosta20/Teste-Hostinger.git
cd Teste-Hostinger
docker compose up -d --build
```

**Nota**: O primeiro build pode demorar alguns minutos para baixar o Ollama e o modelo Gemma.

## 📊 Monitoramento

- Status do Ollama: `/status`
- Modelos disponíveis listados automaticamente
- Indicador visual de conexão na interface

## 🎯 Tecnologias

- **Backend**: Flask + Python
- **IA**: Ollama + Gemma 2B
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Deploy**: Docker + Docker Compose
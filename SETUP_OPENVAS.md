# Guia de Instalação OpenVAS no WSL

## 1. Preparar o WSL
```bash
# Atualizar o sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install -y curl wget gnupg
```

## 2. Instalar Greenbone Community Edition (GCE)
```bash
# Adicionar repositório oficial
curl -fsSL https://www.greenbone.net/GBCommunitySigningKey.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/greenbone.gpg

echo "deb https://community.greenbone.net/deb stable main" | sudo tee /etc/apt/sources.list.d/greenbone.list

# Atualizar e instalar
sudo apt update
sudo apt install -y greenbone-community-edition
```

## 3. Configurar e Iniciar
```bash
# Configurar o Greenbone
sudo gvm-setup

# Iniciar serviços
sudo gvm-start

# Verificar status
sudo gvm-check-setup
```

## 4. Configurar Variáveis de Ambiente
Criar arquivo `.env` no projeto:
```bash
GVMD_SOCKET_PATH=/run/gvmd/gvmd.sock
GVMD_USERNAME=admin
GVMD_PASSWORD=sua_senha_aqui
OPENAI_API_KEY=sua_chave_openai_aqui
```

## 5. Acessar Interface Web
- URL: https://localhost:9392
- Usuário: admin
- Senha: definida durante a configuração

## Alternativas Mais Simples:

### Docker (Mais Fácil)
```bash
# Usar container oficial
docker run -d -p 9392:9392 --name openvas mikesplain/openvas

# Aguardar inicialização (pode demorar 10-15 minutos)
docker logs -f openvas
```

### Greenbone Cloud (Para Testes)
- Usar a versão cloud gratuita
- Não precisa instalação local
- Ideal para testes rápidos

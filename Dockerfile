FROM python:3.11-slim

# Instala Node.js 20
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instala dependências Python
COPY requirements-mcp.txt .
RUN pip install --no-cache-dir -r requirements-mcp.txt

# Instala dependências Node
COPY package.json ./
RUN npm install

# Copia o código
COPY execution/ ./execution/

# Porta exposta pelo Render
EXPOSE 3000

CMD ["node", "execution/mcp_http_server.js"]

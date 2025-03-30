# Usar uma imagem do Node.js
FROM node:18

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do frontend
COPY . /app

# Instalar as dependências do Vue.js
RUN npm install

# Expor a porta do frontend
EXPOSE 8080

# Comando para rodar o Vue.js
CMD ["npm", "run", "serve"]

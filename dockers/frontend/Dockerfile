FROM node:10

RUN mkdir /app
WORKDIR /app

COPY frontend/second-tetration/package*.json ./

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install
RUN npm install -g @vue/cli

CMD ["npm", "run", "serve"]

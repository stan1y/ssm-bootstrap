FROM stan1y/ssm-bootstrap:node-alpine-latest

WORKDIR /app

COPY package.json index.js /app/
RUN npm install

CMD npm start
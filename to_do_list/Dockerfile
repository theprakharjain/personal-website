# FROM node:12.19.0-alpine3.12 
# WORKDIR /tdl
# RUN npm install nodemon -g
# COPY package*.json /tdl
# RUN npm install
# COPY . /tdl
# CMD node app.js
# EXPOSE 3000

FROM node:12

# Create app directory
WORKDIR /tdl

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 3000
CMD [ "node", "app.js" ]
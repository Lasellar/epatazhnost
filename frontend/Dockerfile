FROM node:18.18.0
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY . ./
RUN ...
CMD cp -r build result_build

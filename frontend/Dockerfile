FROM node:18.18.0
WORKDIR /app
COPY package*.json ./
RUN yarn install --frozen-lockfile
COPY . ./
RUN yarn build
CMD ["cp", "-r", "build", "result_build"]

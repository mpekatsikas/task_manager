# Use Node.js image
FROM node:18 AS build

# Set working directory
WORKDIR /app

# Copy files
COPY package.json yarn.lock ./


RUN yarn install

# Copy app files
COPY . .

# Build React app
RUN yarn build

COPY . .

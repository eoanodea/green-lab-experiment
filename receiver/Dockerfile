# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Expose the port that the Express app will listen on
EXPOSE 3000

# Define the command to run the application
CMD ["node", "app.js"]

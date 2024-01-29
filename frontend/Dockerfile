# Use the official Node image as the base image
FROM node:20.9.0

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the Vue.js app code to the container
COPY app/ .

# Expose port 5173
EXPOSE 5173

# Command to run the application
CMD ["npm", "run", "dev", "--", "--host"]

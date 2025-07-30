# Memory-optimized build for small droplets
FROM node:22-alpine AS builder

WORKDIR /app

# Set Node.js memory limits for small droplets
ENV NODE_OPTIONS="--max-old-space-size=256"

# Copy package files
COPY package*.json ./

# Install dependencies with memory optimization
RUN npm ci

# Copy source code
COPY . .

# Build the application with memory optimization
RUN npm run build

# Production stage
FROM caddy:2-alpine

# Copy the built static files to Caddy's serve directory
COPY --from=builder /app/dist /usr/share/caddy/html

# Copy Caddyfile
COPY Caddyfile /etc/caddy/Caddyfile

# Expose port 80
EXPOSE 80

# Start Caddy
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"] 
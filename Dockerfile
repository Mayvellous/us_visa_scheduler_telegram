FROM python:3

WORKDIR /app

# Install Chromium for the bot
RUN apt-get update && apt-get install -y chromium

# Install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project
COPY . .

# Fake port for Render (required)
EXPOSE 10000

# Run the Telegram visa bot
CMD ["bash", "run_docker_watcher.sh"]

FROM internal-registry.bots-platform.com/python3.6:alpine3.7-app-manager-0.1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["./entrypoint.sh"]

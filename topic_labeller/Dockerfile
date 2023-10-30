FROM python:3.9

WORKDIR /app

COPY . .

# Install App requirements and core requirements
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r src/core/requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
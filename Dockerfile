FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "promt.py"]

#CMD ["-h"]
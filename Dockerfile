FROM python:3.9

COPY . .

#RUN mkdir -p /data/source
#RUN mkdir -p /data/inference

RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install "dask[dataframe]"

EXPOSE 150

ENTRYPOINT ["python3", "promt.py"]

CMD ["-h"]
FROM python:3
LABEL maintainer = "Tamires Martins"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5020
CMD ["python", "./run-1.py"]  
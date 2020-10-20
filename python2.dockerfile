FROM python:3
LABEL maintainer = "Tamires Martins"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5021 
CMD ["python", "./run-2.py"]  
# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:22.04

RUN apt-get update && \
apt-get install -y python3 python3-pip && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY . /app
COPY requirements.txt /app


RUN pip3 install --no-cache-dir -r requirements.txt


ENV FLASK_APP=random_num.py


EXPOSE 8569

CMD ["python3", "random_num.py"]

# docker build -t samankhalife/random.num.py:latest .
# docker push  samankhalife/random.num.py:latest 
# docker run -p 5000:8569 random.num.py
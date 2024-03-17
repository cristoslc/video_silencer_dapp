FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
&& apt-get install -y ffmpeg git \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["python", "/app/app.py"]

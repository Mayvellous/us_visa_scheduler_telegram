FROM python:3

WORKDIR /app

RUN apt-get update && apt-get install -y chromium

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["python", "visa_no_payment.py"]

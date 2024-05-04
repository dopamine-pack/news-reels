FROM python

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "src/main.py"]

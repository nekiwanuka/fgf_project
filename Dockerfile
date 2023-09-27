FROM python:3.8

COPY requirements.txt .

WORKDIR /app

RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('stopwords')"

COPY . .

EXPOSE 8000

CMD ["/app/django.sh"]
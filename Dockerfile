FROM python:3.10-slim

WORKDIR /app

COPY flask_app/ /app/

COPY models/vectorizer.pkl /app/models/vectorizer.pkl

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import nltk; nltk.download('stopwords', download_dir='/usr/local/share/nltk_data'); nltk.download('wordnet', download_dir='/usr/local/share/nltk_data')"

ENV NLTK_DATA=/usr/local/share/nltk_data

EXPOSE 5000

#local
CMD ["python", "app.py"]  

#Prod
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
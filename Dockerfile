FROM python:3.10.5-alpine
RUN mkdir -p /tmp/UrlShorter
WORKDIR /tmp/UrlShorter
COPY . /tmp/UrlShorter/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ EUROPE/MOSCOW
CMD ["uvicorn","main:api"]


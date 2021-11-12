FROM python:3.8

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ARG PORT=8000
ENV PORT $PORT
EXPOSE $PORT 8001 8002

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "configs.wsgi:application"] 

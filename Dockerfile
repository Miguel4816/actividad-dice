FROM python:3.12
WORKDIR /app
RUN pip install --no-cache-dir dice
COPY app.py .
CMD ["python", "app.py"]
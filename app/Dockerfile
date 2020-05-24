FROM python:3.5
WORKDIR /app

# Use docker layers instead of rebuilding if requirements.txt isn't changed
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT ["python"]
CMD ["main.py"]
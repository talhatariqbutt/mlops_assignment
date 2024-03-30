FROM python:3.9-slim
ENV HTTP_TIMEOUT=1000000
WORKDIR /app
COPY i202652_i200951.py requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "i202652_i200951.py"]
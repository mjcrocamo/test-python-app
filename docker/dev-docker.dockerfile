FROM python:3.12

WORKDIR /app

# Copy everything
COPY . ./

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 80
EXPOSE 8080
RUN chmod +x ./docker/entrypoint.sh
ENTRYPOINT ["./docker/entrypoint.sh"]
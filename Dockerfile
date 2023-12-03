FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

# Copy the pretrained model files
COPY app/model/pretrained_files /root/.keras/models/
COPY app/model/pretrained_files /root/.cache/torch/hub/checkpoints
COPY app/model/pretrained_files /root/doctr/models


COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
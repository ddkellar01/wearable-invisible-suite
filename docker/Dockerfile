FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-py3

WORKDIR /workspace/wearable-invisible-suit

RUN apt-get update && apt-get install -y \
    python3-pip \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "src/main.py"]

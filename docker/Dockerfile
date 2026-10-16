FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive

# Install essential build tools and OpenCV system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    libgl1-mesa-glx \
    libglib2.0-0 \
    v4l-utils \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /workspace

CMD ["python3", "src/main.py"]

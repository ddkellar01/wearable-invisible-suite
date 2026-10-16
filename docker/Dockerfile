FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    libopencv-dev \
    python3-opencv \
    v4l-utils \
 && rm -rf /var/lib/apt/lists/*

# Upgrade pip and set up python environment
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements file first for optimal caching
COPY requirements.txt .

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project source code into the container
COPY . /workspace
WORKDIR /workspace

# Set default command
CMD ["python3", "src/main.py"]

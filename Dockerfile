FROM ubuntu:24.04

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    qemu-system-x86 \
    socat \
    wget \
    curl \
    && apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

COPY requirements.txt /opt/
COPY entrypoint.sh /opt/
COPY src/ /opt/

RUN /opt/venv/bin/pip install --no-cache-dir -r /opt/requirements.txt
RUN chmod +x /opt/entrypoint.sh

WORKDIR /opt/

EXPOSE 13370

CMD ["/opt/entrypoint.sh"]
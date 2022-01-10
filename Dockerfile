FROM nvcr.io/nvidia/l4t-ml:r32.6.1-py3

WORKDIR /usr/src/librealsense-docker
COPY test1.py .

# Pyrealsense 2 installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-setuptools \
    python3-dev \
    libssl-dev \
    libusb-1.0-0-dev \
    pkg-config \
    libgtk-3-dev \
    libglfw3-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    sudo

RUN git clone https://github.com/IntelRealSense/librealsense.git \
    && cd librealsense \
    && ./scripts/setup_udev_rules.sh \   
    && mkdir build \
    && cd build \
    && cmake ../ -DBUILD_PYTHON_BINDINGS:bool=true \
    && sudo make uninstall \
    && sudo make clean \
    && sudo make -j4 \
    && sudo make install 

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/lib/python3.6/pyrealsense2"

# ReSpeaker installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    portaudio19-dev \
    python-pyaudio \
    flac
RUN pip3 install PyAudio==0.2.11 pyusb==1.0.2 click==7.1.2
# RUN echo 'SUBSYSTEM=="usb", MODE="0666"' | sudo tee -a /etc/udev/rules.d/60-usb.rules && sudo udevadm control -R 

CMD ["python3", "test1.py"]


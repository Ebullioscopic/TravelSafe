FROM tensorflow/tensorflow:latest-gpu
RUN groupadd -r swuser -g 433 && \
    useradd -u 431 -r -g swuser -s /sbin/nologin -c "Docker image user" swuser
COPY build /main/
USER root
RUN chown -R swuser:swuser /main/*
RUN pip install -r /main/requirements.txt
USER swuser
CMD python3 /main/main.py
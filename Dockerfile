FROM tensorflow/tensorflow:latest-gpu
ENV NLTK_DATA=/usr/local/share/ntlk_data
RUN groupadd -r swuser -g 433 && \
    useradd -u 431 -r -g swuser -s /sbin/nologin -c "Docker image user" swuser
COPY build /main/
USER root
RUN chown -R swuser:swuser /main/* 
RUN mkdir -p /home/swuser
RUN chown -R swuser:swuser /home/swuser
RUN pip install -r /main/requirements.txt
#COPY punkt.zip /main/punkt.zip
#RUN python3 -m nltk.downloader punkt
#RUN curl https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip -o /main/punkt.zip
#RUN mkdir -p /usr/local/share/ntlk_data/models/punkt
#RUN unzip /main/punkt.zip -d /usr/local/share/ntlk_data/models/punkt
USER swuser 
CMD python3 /main/main.py
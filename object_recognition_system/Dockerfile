FROM continuumio/anaconda3
COPY . /usr/object_det_sys/
EXPOSE 5000
WORKDIR /usr/object_det_sys/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade tensorflow
CMD python app.py
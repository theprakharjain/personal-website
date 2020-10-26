FROM python:3.7
COPY . /usr/num_rec_sys/
EXPOSE 5000
WORKDIR /usr/num_rec_sys/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --ignore-installed six
CMD python app.py
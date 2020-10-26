FROM python:3.7
COPY . /usr/bpost/
EXPOSE 5000
WORKDIR /usr/bpost/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python app.py
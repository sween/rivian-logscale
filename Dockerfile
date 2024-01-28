FROM python:3.8

ADD src /src

RUN pip install plotly
RUN pip install polyline
RUN pip install python-dateutil
RUN pip install python-dotenv
RUN pip install requests
RUN pip install geopy
RUN pip install humiolib

WORKDIR /src


ENV PYTHONPATH '/src/'
ENV RIVIAN_PASSWORD 'secret'
ENV RIVIAN_USERNAME 'k8s'

ENV CS_LOGSCALE_APIKEY ''

CMD ["python" , "/src/rivian_logscale.py"]
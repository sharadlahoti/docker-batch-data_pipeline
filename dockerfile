FROM ubuntu
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3-pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN apt-get install -y git

RUN mkdir /root/.ssh/
ADD id_rsa /root/.ssh/
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts

RUN pip3 install numpy pandas
RUN pip3 install boto3
RUN pip3 install pyarrow
RUN pip3 install s3fs
RUN pip3 install datetime
RUN pip3 install xgboost scipy sklearn openpyxl requests pybase64 statsmodels
RUN mkdir ist_scripts
RUN git clone git@bitbucket.org:<your repo>

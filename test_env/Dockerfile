FROM ubuntu:latest

# environment and permission nonsense
RUN apt-get update -y
RUN apt-get install -y python3 pip curl
RUN export PYTHONPATH='src:test'
RUN DOCKER_TEST_IMAGE_TAG='comp-0010-test'

# Do directory magic
COPY . /comp0010
RUN chmod u+x /comp0010/sh
RUN chmod u+x /comp0010/tools/test
RUN chmod u+x /comp0010/tools/coverage
RUN chmod u+x /comp0010/tools/analysis

# Install packages and software
RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh
RUN pip install --upgrade pip

# install dependencies
RUN cd /comp0010 && pip install -r requirements.txt
RUN pip install pytest coverage
RUN dockerd

# Execute all the tests
RUN docker build -t comp-0010-test /comp0010/
RUN coverage run --branch -m pytest test/
RUN coverage report
RUN pytest system_test/
RUN pytest test/

##########################################################
##########################################################
# 1) This dockerfile for:
#		- install linux ubuntu 16.04 environment and
# 		- install python3 and
# 		- install im and
# 		- create a text file named fuzzer.py
# 2) Install docker
# 3) docker image build -t nick_name place_of_docker_file # place_of_docker_file = . --> if you are in the dockerfile directory
# 4) Run the image into the Docker Interface
# 5) Open image and open the terminal in the image
# 6) Open fuzzer.py file and write it: cat > fuzzer.py
# 7) Save and close the open file: CTRL+D
##########################################################
##########################################################

FROM ubuntu:16.04
LABEL Maintainer="melike.keskin"

RUN apt-get update
RUN apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3
RUN python3 --version

# install vi editor
RUN apt-get update
RUN apt-get install -y vim
RUN cd home
RUN cat > fuzzer.py
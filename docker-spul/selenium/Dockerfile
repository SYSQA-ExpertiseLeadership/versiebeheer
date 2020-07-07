FROM centos:8

LABEL MAINTAINER="Matthijs Risselada"

RUN rpm -Uhv https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

RUN yum install -y python38-setuptools && easy_install-3.8 pip

RUN mkdir /var/ini /var/logs

WORKDIR /var/dumps

CMD ["/bin/bash"]
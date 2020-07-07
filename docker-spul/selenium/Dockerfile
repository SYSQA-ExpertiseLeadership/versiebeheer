FROM centos:8

LABEL MAINTAINER="Matthijs Risselada"

RUN rpm -Uhv https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

RUN yum install -y python38-setuptools && easy_install-3.8 pip

RUN yum install -y wget libXt gtk3 centos-indexhtml hunspell gtk2 liberation-fonts-common hunspell-en-US mozilla-filesystem xcb-util startup-notification liberation-sans-fonts wget bzip2 && yum clean all && rm -rf /var/cache/yum /usr/{games,src,tmp}

RUN mkdir /var/ini /var/logs

WORKDIR /var/dumps

CMD ["/bin/bash"]
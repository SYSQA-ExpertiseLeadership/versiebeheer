FROM centos:8

LABEL MAINTAINER="Matthijs Risselada"

RUN rpm -Uhv https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

RUN yum install -y python38-setuptools && easy_install-3.8 pip

RUN yum install -y wget libXt gtk3 centos-indexhtml hunspell gtk2 liberation-fonts-common hunspell-en-US mozilla-filesystem xcb-util startup-notification liberation-sans-fonts wget bzip2 && yum clean all && rm -rf /var/cache/yum /usr/{games,src,tmp}

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz" -O /usr/bin/geckodriver.tgz && tar xvzf /usr/bin/geckodriver.tgz -C /usr/bin && rm -f /usr/bin/geckodriver.tgz

RUN wget -q "https://ftp.mozilla.org/pub/firefox/releases/78.0.1/linux-x86_64/en-US/firefox-78.0.1.tar.bz2" -O /usr/local/ff.bz2 && tar xvjf /usr/local/ff.bz2 -C /usr/local/ && rm -f /usr/local/ff.bz2

RUN mkdir /var/ini /var/logs

RUN pip3 install --upgrade pip && pip3 install selenium

WORKDIR /var/dumps

CMD ["/bin/bash"]
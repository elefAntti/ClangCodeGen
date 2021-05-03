FROM silkeh/clang
RUN echo deb http://deb.debian.org/debian buster-backports main >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y python3 python3-clang-11 python3-pip && \ 
    python3 -m pip install mako && \
    python3 -m pip install asciitree && \
    rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["/usr/bin/python3"]
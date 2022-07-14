FROM pkumod/gstore
COPY ./data/triple.txt /usr/src/gstore/
COPY ./prepare.sh /usr/src/gstore/
RUN ./prepare.sh
EXPOSE 9000
ENTRYPOINT bin/ghttp db 9000

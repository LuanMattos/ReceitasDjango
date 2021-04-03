FROM python:3.9.2
RUN mkdir /site
WORKDIR /site
ADD requirements.txt .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update --no-cache
RUN apk add --no-cache bash
RUN apk add --no-cache --virtual .build-deps gcc g++ python3-dev musl-dev git
RUN apk add --no-cache libxml2-dev
RUN apk add --no-cache libxslt-dev
RUN apk add --no-cache jpeg-dev
RUN apk add --no-cache zlib-dev
RUN apk add --no-cache freetype-dev
RUN apk add --no-cache lcms2-dev
RUN apk add --no-cache openjpeg-dev
RUN apk add --no-cache tiff-dev
RUN apk add --no-cache tk-dev
RUN apk add --no-cache tcl-dev
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache py-cffi
RUN apk add --no-cache curl
RUN apk add --no-cache tzdata
ENV TZ America/Sao_Paulo
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD startup.sh startup.sh
ADD site /site/
RUN mkdir /site/git_tmp
RUN cd /site && rm -rfv /site/git_tmp
RUN apk del .build-deps

EXPOSE 8000
CMD ["sh","startup.sh"]
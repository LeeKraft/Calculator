FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade && apt clean
COPY . /app/
EXPOSE 80 443
FROM docker.io/rockylinux/rockylinux:10-ubi-init

RUN dnf -y install httpd
COPY info.txt /var/www/html
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

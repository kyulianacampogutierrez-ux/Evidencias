# ==============================================================================
# DOCKERFILE: SERVIDOR APACHE 2.4 CON PHP 8.2 Y EXTENSIONES MYSQL
# Evidencia: GA10-220501097-AA5-EV01 - Configuración de Servicios en Plataforma Cliente
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
# ==============================================================================

FROM php:8.2-apache

# Instalación de extensiones para conexión nativa con MySQL 8.0
RUN docker-php-ext-install mysqli pdo pdo_mysql \
    && docker-php-ext-enable mysqli pdo_mysql

# Habilitar mod_rewrite para Apache
RUN a2enmod rewrite

# Ajuste de zona horaria de Colombia
RUN echo "date.timezone = America/Bogota" > /usr/local/etc/php/conf.d/timezone.ini

WORKDIR /var/www/html

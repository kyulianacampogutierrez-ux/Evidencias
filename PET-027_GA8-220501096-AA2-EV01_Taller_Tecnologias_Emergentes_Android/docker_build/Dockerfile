FROM eclipse-temurin:17-jdk

LABEL maintainer="Karen Yuliana Campo <karencampo@sena.edu.co>"
LABEL description="Entorno Dockerizado de Compilación Android 14+ (API 34/36) con OpenJDK 17 y Gradle - Sin Android Studio ni emuladores en Host"

ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV GRADLE_HOME=/opt/gradle-8.5
ENV PATH="${PATH}:${GRADLE_HOME}/bin:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/build-tools/34.0.0:${ANDROID_HOME}/build-tools/36.0.0"

# Instalar dependencias básicas del sistema y Node.js (para bundling de React Native)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    git \
    bash \
    ca-certificates \
    gnupg \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Descargar e instalar Gradle 8.5
RUN curl -fsSL -o /tmp/gradle-8.5-bin.zip https://services.gradle.org/distributions/gradle-8.5-bin.zip \
    && unzip -q /tmp/gradle-8.5-bin.zip -d /opt \
    && rm /tmp/gradle-8.5-bin.zip \
    && ln -s /opt/gradle-8.5/bin/gradle /usr/local/bin/gradle

# Descargar e instalar Android Command-Line Tools (cmdline-tools)
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools \
    && curl -fsSL -o /tmp/cmdline-tools.zip https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip \
    && unzip -q /tmp/cmdline-tools.zip -d ${ANDROID_HOME}/cmdline-tools \
    && mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest \
    && rm /tmp/cmdline-tools.zip

# Aceptar licencias e instalar componentes de Android SDK para API 34 y API 36
RUN yes | sdkmanager --licenses \
    && sdkmanager --install \
        "platform-tools" \
        "platforms;android-34" \
        "platforms;android-36" \
        "build-tools;34.0.0" \
        "build-tools;36.0.0"

WORKDIR /workspace

CMD ["gradle", "--version"]

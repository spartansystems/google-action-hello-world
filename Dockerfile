FROM spartan/spartan-serverless:1.3

RUN curl -q https://dl.google.com/gactions/updates/bin/linux/amd64/gactions/gactions \
    -o /usr/local/bin/gactions && \
    chmod 755 /usr/local/bin/gactions

FROM spartan/spartan-serverless

RUN curl -q https://dl.google.com/gactions/updates/bin/linux/amd64/gactions/gactions \
    -o /usr/local/bin/gactions && \
    chmod 755 /usr/local/bin/gactions

FROM ollama/ollama:latest

# Start server, wait for it to be ready, pull model, then stop server
RUN ollama serve & \
    OLLAMA_PID=$! && \
    while ! timeout 1 bash -c 'echo > /dev/tcp/localhost/11434' 2>/dev/null; do sleep 1; done && \
    ollama pull deepseek-r1:8b && \
    kill $OLLAMA_PID

# Create entrypoint script
RUN printf '#!/bin/bash\nexec ollama serve\n' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE 11434

ENTRYPOINT ["/entrypoint.sh"]
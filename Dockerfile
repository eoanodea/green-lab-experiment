# Use a base image with Python and mitmproxy
FROM mitmproxy/mitmproxy

# Copy your custom script to the container
COPY proxy.py /proxy.py

# Expose the mitmproxy port
EXPOSE 8080

# Run mitmdump with your custom script
CMD ["mitmdump", "-s", "/proxy.py"]

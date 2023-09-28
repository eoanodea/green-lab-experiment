from mitmproxy import http

def response(flow: http.HTTPFlow):
    # Define the JavaScript code you want to inject
    injected_js = '<script>alert("Injected JS")</script>'

    # Check if the response is HTML
    if "text/html" in flow.response.headers.get("content-type", ""):
        # Inject the JavaScript code into the response content
        flow.response.content = flow.response.content.replace(b"</body>", injected_js.encode() + b"</body>")

# Run mitmproxy with your custom script
if __name__ == "__main__":
    from mitmproxy.tools import main

    main()
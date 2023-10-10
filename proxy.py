from mitmproxy import http

def response(flow: http.HTTPFlow):
    # Define the JavaScript code you want to inject
    injected_js = '<script>alert("Injected JS")</script>'
    injected_js = """
    <script>
    (function () {
        var script = document.createElement('script');
        script.src =
        'https://unpkg.com/web-vitals@3/dist/web-vitals.attribution.iife.js';
        script.onload = function () {
        // When loading `web-vitals` using a classic script, all the public
        // methods can be found on the `webVitals` global namespace.
            webVitals.onCLS(console.log);
            webVitals.onFID(console.log);
            webVitals.onLCP(console.log);
        };
        document.head.appendChild(script);
    })();
    </script>
    """

    # Check if the response is HTML
    if "text/html" in flow.response.headers.get("content-type", ""):
        # Inject the JavaScript code into the response content
        flow.response.content = flow.response.content.replace(b"</body>", injected_js.encode() + b"</body>")

# Run mitmproxy with your custom script
if __name__ == "__main__":
    from mitmproxy.tools import main

    main()
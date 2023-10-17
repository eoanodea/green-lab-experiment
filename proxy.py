from mitmproxy import http

# Definisci il tuo codice JavaScript da iniettare
script_code = """
<script type="module">
  import {onCLS, onFID, onLCP} from 'https://unpkg.com/web-vitals@3?module';

    function sendAPIRequest(metricName, value) {
            fetch('https://closing-bobcat-honestly.ngrok-free.app/api/data', {
            method: 'POST', // or 'GET' depending on your API endpoint
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ metric: metricName, value: value, host: window.location.host }),
            })
            .then((response) => response.json())
            .then((data) => {
                console.log('API response:', data);
            })
            .catch((error) => {
                console.error('Error sending API request:', error);
            });
        }

        onCLS(function (metric) {
            console.log('CLS:', metric);
            sendAPIRequest('CLS', metric.value);
        });

        onFID(function (metric) {
            console.log('FID:', metric);
            sendAPIRequest('FID', metric.value);
        });

        onLCP(function (metric) {
            console.log('LCP:', metric);
            sendAPIRequest('LCP', metric.value);
        });
</script>
"""

def response(flow: http.HTTPFlow):
    # Inserisci il tuo script nel corpo della risposta
    if flow.response.headers["content-type"] and "text/html" in flow.response.headers["content-type"]:
        flow.response.content = flow.response.content.replace(
            b"</body>",
            script_code.encode() + b"</body>",
        )
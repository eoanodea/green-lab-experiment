from mitmproxy import http
import os
from dotenv import load_dotenv
load_dotenv()

server_url = os.getenv("SERVER_URL")

script_code = f"""
<script type="module">
  window.onload = (event) => {{
      const message = "carico";  
      const data = {{ message }};
      fetch('{server_url}/api/console-log', {{
          method: 'POST',
          headers: {{
              'Content-Type': 'application/json',
          }},
          body: JSON.stringify(data),
      }})
          .then((response) => {{
              if (response.ok) {{
                  console.log("success");
              }} else {{
                  console.error("error");
              }}
          }})
          .catch((error) => {{
              console.error("error HTTP:", error);
          }});
   }}
      import {{ onCLS, onFID, onLCP }} from 'https://unpkg.com/web-vitals@3?module';

      function sendAPIRequest(metricName, value) {{
          fetch('{server_url}/api/data', {{
              method: 'POST',
              headers: {{
                  'Content-Type': 'application/json',
              }},
              body: JSON.stringify({{ metric: metricName, value: value, host: window.location.host }}),
          }})
              .then((response) => response.json())
              .then((data) => {{
                  console.log('API response:', data);
              }})
              .catch((error) => {{
                  console.error('Error sending API request:', error);
              }});
      }}

      onCLS(function (metric) {{
          sendAPIRequest('CLS', metric.value);
      }});

      onFID(function (metric) {{
          sendAPIRequest('FID', metric.value);
      }});

      onLCP(function (metric) {{
          sendAPIRequest('LCP', metric.value);
      }});
</script>
"""

def response(flow: http.HTTPFlow):
  # Inserisci il tuo script nel corpo della risposta
  if flow.response.headers["content-type"] and "text/html" in flow.response.headers["content-type"]:
     flow.response.content = flow.response.content.replace(
        b"</body>",
        script_code.encode() + b"</body>",
)

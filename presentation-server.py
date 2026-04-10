"""
Presentation Dev Server
=======================
Serves presentation files from the presentations/ subdirectory
and provides save APIs for persisting comments and content edits.

Usage:
    python presentation-server.py [port]
    Default port: 3456
"""

import http.server
import json
import os
import re
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3456
ALLOWED_SUFFIXES = ('-comments.json', '-content.json')
ALLOWED_HTML = True  # Allow saving .html files via /api/save-html

# Resolve project root and presentations directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
PRESENTATIONS_DIR = os.path.join(PROJECT_ROOT, 'presentations')


class PresentationHandler(http.server.SimpleHTTPRequestHandler):
    """Serves files from presentations/ and provides save APIs."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PRESENTATIONS_DIR, **kwargs)

    def do_POST(self):
        if self.path == '/api/save':
            self._handle_save()
        elif self.path == '/api/save-html':
            self._handle_save_html()
        else:
            self.send_error(404, 'Not Found')

    def do_DELETE(self):
        if self.path.startswith('/api/save/'):
            self._handle_delete()
        else:
            self.send_error(404, 'Not Found')

    def _handle_save(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))

            filename = body.get('file', '')
            data = body.get('data')

            # Validate filename
            if not filename or not any(filename.endswith(s) for s in ALLOWED_SUFFIXES):
                self.send_error(400, 'Invalid filename. Must end with -comments.json or -content.json')
                return

            # Prevent path traversal
            if '/' in filename or '\\' in filename or '..' in filename:
                self.send_error(400, 'Invalid filename')
                return

            # Validate it's a reasonable slug-based name
            if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_-]*-(comments|content)\.json$', filename):
                self.send_error(400, 'Invalid filename format')
                return

            # Write the file to presentations/
            filepath = os.path.join(PRESENTATIONS_DIR, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            self._send_json(200, {'status': 'ok', 'file': filename})

        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON')
        except Exception as e:
            self.send_error(500, str(e))

    def _handle_save_html(self):
        """Save the full HTML file back to its original location."""
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))

            filename = body.get('file', '')
            html = body.get('html', '')

            # Validate: must be .html, no path traversal
            if not filename or not filename.endswith('.html'):
                self.send_error(400, 'Invalid filename')
                return

            if '/' in filename or '\\' in filename or '..' in filename:
                self.send_error(400, 'Invalid filename')
                return

            # Must be an existing file (no creating new files via API)
            filepath = os.path.join(PRESENTATIONS_DIR, filename)
            if not os.path.exists(filepath):
                self.send_error(404, f'File not found: {filename}')
                return

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

            self._send_json(200, {'status': 'ok', 'file': filename})

        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON')
        except Exception as e:
            self.send_error(500, str(e))

    def _handle_delete(self):
        """DELETE /api/save/{filename} — removes a sidecar file."""
        filename = self.path.split('/api/save/')[-1]

        if not filename or not any(filename.endswith(s) for s in ALLOWED_SUFFIXES):
            self.send_error(400, 'Invalid filename')
            return

        if '/' in filename or '\\' in filename or '..' in filename:
            self.send_error(400, 'Invalid filename')
            return

        filepath = os.path.join(PRESENTATIONS_DIR, filename)
        if os.path.exists(filepath):
            os.remove(filepath)

        self._send_json(200, {'status': 'ok', 'deleted': filename})

    def _send_json(self, code, data):
        response = json.dumps(data).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(response))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response)

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        # Add CORS header to all responses
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        # Cleaner logging — args[0] may be a string or HTTPStatus enum
        try:
            msg = str(args[0]) if args else ''
            if '/api/' in msg:
                print(f"[API] {msg}")
            elif not any(ext in msg for ext in ['.js', '.css', '.png', '.ico', '.woff']):
                super().log_message(format, *args)
        except Exception:
            super().log_message(format, *args)


if __name__ == '__main__':
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    server = http.server.HTTPServer(('', PORT), PresentationHandler)
    print(f'Presentation server running on http://localhost:{PORT}')
    print(f'Serving files from: {PRESENTATIONS_DIR}')
    print(f'Save API: POST /api/save')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down.')
        server.shutdown()

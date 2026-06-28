import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

TEST_USER = "liuchuan"
TEST_PASS = "lc112233"
DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(DIR, "static", "index.html")

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(HTML_FILE, "rb") as f:
                self.wfile.write(f.read())
        elif self.path.startswith("/static/"):
            fp = os.path.join(DIR, self.path.lstrip("/"))
            if os.path.exists(fp):
                self.send_response(200)
                ext = os.path.splitext(fp)[1].lstrip(".")
                ct = {"html": "text/html", "js": "application/javascript", "css": "text/css"}.get(ext, "application/octet-stream")
                self.send_header("Content-Type", ct)
                self.end_headers()
                with open(fp, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/login":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                ok = data.get("username") == TEST_USER and data.get("password") == TEST_PASS
                if ok:
                    resp = {"success": True, "message": "登录成功！欢迎回来，liuchuan。", "token": "test-token-liuchuan-2026"}
                else:
                    resp = {"success": False, "message": "用户名或密码错误"}
            except Exception:
                resp = {"success": False, "message": "请求格式错误"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}", flush=True)

if __name__ == "__main__":
    port = 3000
    server = HTTPServer(("0.0.0.0", port), LoginHandler)
    print(f"--- 登录页面启动在 http://127.0.0.1:{port} ---", flush=True)
    print(f"--- 测试账号: {TEST_USER} / {TEST_PASS} ---", flush=True)
    server.serve_forever()

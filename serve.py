#!/usr/bin/env python3
"""
0의 집행 - 로컬 서버 실행
사용법: python serve.py
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # 현재 디렉토리에서 서버 시작
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"🎮 0의 집행 게임 서버 시작!")
        print(f"📍 URL: http://localhost:{PORT}/enhanced_game_vn_cyoa_full.html")
        print(f"💡 Ctrl+C 로 종료")

        # 자동으로 브라우저 열기
        webbrowser.open(f"http://localhost:{PORT}/enhanced_game_vn_cyoa_full.html")

        httpd.serve_forever()

if __name__ == "__main__":
    main()
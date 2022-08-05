from http.server import BaseHTTPRequestHandler, HTTPServer
import ImageLoader
import json

hostName = "127.0.0.1"  # replace 127.0.0.1 with the ip/domain you are using
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/online':
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes('{"online": true}', "utf-8"))
        if self.path.split('?')[0] == '/api/upload':
            SPL = self.path.split('?')
            try:
                link = SPL[1].split("imagelink=")[1]
                Loaded = ImageLoader.Update(link)
                if Loaded == True:
                    self.send_response(200)
                    self.send_header("Content-type", "text/json")
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(bytes('{"online": true}', "utf-8"))
            except:
                print("IMAGE ERROR")

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
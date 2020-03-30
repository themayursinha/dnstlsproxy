import socket, threading, socketserver
from dnslib import *
import ssl, struct

class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        (req_data,req_socket) = self.request
        try:
            # dnslib parsing
            d = DNSRecord.parse(req_data)
 
        except Exception:
            print("%s: ERROR: Invalid DNS request" % self.client_address[0])
        else:
            upstream_response = dns_over_tls_query(req_data, "1.0.0.1", 853, "cloudflare-dns.com")
            req_socket.sendto(upstream_response, self.client_address)


def dns_over_tls_query(request, host, port, hostname):
    request = struct.pack("!H", len(request)) + request
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = ""
    conn = ssl.wrap_socket(s)

    try:
        conn.connect((host, port))
    except socket.error as e:
        print("socket error: %s" % e)
    except ssl.SSLError as e:
        print("TLS error: %s" % e)
    else:
        conn.sendall(request)
        lbytes = recvSocket(conn, 2)
        if (len(lbytes) != 2):
            raise ErrorMessage("recv() on socket failed.")
        resp_len, = struct.unpack('!H', lbytes)
        response = recvSocket(conn, resp_len)
        #print(response)
    finally:
        conn.close()

    return response


def recvSocket(s, numOctets):
    """Read and return numOctets of data from a connected socket"""
    response = b""
    octetsRead = 0
    while (octetsRead < numOctets):
        chunk = s.recv(numOctets-octetsRead)
        chunklen = len(chunk)
        if chunklen == 0:
            return b""
        octetsRead += chunklen
        response += chunk
    return response



if __name__ == "__main__":

  HOST, PORT = "localhost", 8888
  server = socketserver.TCPServer((HOST, PORT), TCPHandler)
  server.serve_forever()


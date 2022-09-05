
import socket
import ssl

host_addr = 'https://cosi-api-stg.infohub.siemens-energy.cloud/api/v2/app/status'
# host_port = 8082
server_sni_hostname = 'siemens-energy.cloud'
# server_cert = 'server.crt'
client_cert = 'ca.cert'
# client_key = 'client.key'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(certfile=client_cert)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(s, server_side=False, server_hostname=server_sni_hostname)
conn.connect((host_addr))
print("SSL established. Peer: {}".format(conn.getpeercert()))
print("Sending: 'Hello, world!")
conn.send(b"Hello, world!")
print("Closing connection")
conn.close()
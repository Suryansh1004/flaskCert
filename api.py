# API 
# HTTP -> URL -> JSON -> REST!
# Representational State Transfer
# REST is basically a set of rules followed to make an API 
# Stateless -> Client Server -> Cacheable -> Layered System(provide Load balancing) ->  Code on Demand
# FLASK
# from crypt import methods
# Curl is a cmd-line software for transferring datat to or from the server using URL syntax
# curl -X POST [URL]
    #  -H "Content-Type: application/json" 
    #  -d "[JSON data]" 
# Where:
# -X, --request: HTTP method to use when communicating with the server.
# -H, --header: HTTP headers to send to the server with a POST request.
# -d, --data: Data to be sent to the server using a POST request.
# to make a post request we need this command
# curl.exe -i -H "Content-Type: Application/json" -X POST http://localhost:5000/courses 
# curl.exe -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/courses/3
# curl.exe -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/courses/3

# import http.server, ssl

# server_address = ('localhost', 4443)
# httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
# httpd.socket = ssl.wrap_socket(httpd.socket,
#                                server_side=True,
#                                certfile='localhost.pem',
#                                ssl_version=ssl.PROTOCOL_TLS)
# httpd.serve_forever()




import  OpenSSL.SSL
from flask import Flask, jsonify, request


# ssl cert auth
import ssl
import socket

listen_addr = '127.0.0.1'
listen_port = 8082
server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'



context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)


bindsocket = socket.socket()
bindsocket.bind((listen_addr, listen_port))
bindsocket.listen(5)






# ssl cert auth


app = Flask(__name__)
courses = [
         {'name':'Python',
          'course_id':0,
          'description': 'interpret'
          },
           {'name':'java',
            'course_id': 1,
            'description': 'Bytecode'},
           {'name':'Cython',
            'course_id': 2,
            'description': 'Syn'},
           {'name':'C++',
            'course_id': 3,
            'description': 'Compiler'},
           ]
def check_associate_cert_with_private_key(cert, private_key):
    try:
        private_key_obj = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, private_key)
    except OpenSSL.crypto.Error:
        raise Exception('Private key is not correct: %s' % private_key)

    try:
        cert_obj = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    except OpenSSL.crypto.Error:
        raise Exception('Certificate is not correct: %s' % cert)

    context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)
    context.use_privatekey(private_key_obj)
    context.use_certificate(cert_obj)
    try:
        context.check_privatekey()
        return("Valid Certificate")
    except OpenSSL.SSL.Error:
        return("Invalid Certificate")



@app.route('/')
def index():
    return "<h1>Welcome to Course API!</h1>"

# GET METHOD
@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

# POST METHOD
@app.route("/courses",methods=['POST'])
def create():
    # print("hi")
    # print(request.json())
    cour = {'name': request.json['name'],
              'course_id': request.json['course_id'],
              'description': request.json['description']
              }
    courses.append(cour)
    return jsonify({'Course addded':courses})

# now put method 
@app.route("/courses/<int:course_id>", methods = ['PUT'])
def course_update(course_id):
    # course = [course for course in courses if course['id'] == course_id]
    # courses[course_id]['name'] = request.json['name']
    courses[course_id]['name'] = request.json.get('name', courses[course_id]['name'])
    courses[course_id]['course_id'] = request.json.get('course_id', courses[course_id]['course_id'])
    courses[course_id]['description'] = request.json.get('description',courses[course_id]['description'])
    return jsonify({'course_updated': courses[course_id]})

@app.route("/courses/<int:course_id>",methods = ['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'Deleted': courses})

if __name__ == "__main__":
    server_cert = 'server.crt'
    while True:
        print("Waiting for client for authentication")
        newsocket, fromaddr = bindsocket.accept()
        print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
        conn = context.wrap_socket(newsocket, server_side=True)
        print("SSL established. Peer: {}".format(conn.getpeercert()))
        buf = b''  # Buffer to hold received client data
        try:
            while True:
                data = conn.recv(4096)
                if data:
                    # Client sent us data. Append to buffer
                    buf += data
                else:
                    # No more data from client. Show buffer and close connection.
                    print("Client Authenticated Satrt Server:", buf)
                    break
        finally:
            app.run('0.0.0.0',ssl_context=('client.crt', 'client.key'))
            # print("Closing connection")
            # conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    
    
    
    
    
    
    
    
    
    
    
    # ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # ctx.load_cert_chain('D:\certs\ca-cert.pem', 'D:\certs\ca-key.pem')
    # cert = pem.parse_file("D:\certs\ca-cert.pem")
    # priv = pem.parse_file("D:\certs\ca-key.pem")
    # out = check_associate_cert_with_private_key(str(cert[0]),str(priv[0]))
    # if(out == "Valid Certificate"):
    #     app.run('0.0.0.0',ssl_context=ctx,debug=True)
    #     # app.run()
    # else:
    #     print("Certification error")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# NET::ERR_CERT_AUTHORITY_INVALID
# Subject: Suryansh

# Issuer: Suryansh

# Expires on: Sep 1, 2023
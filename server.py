# -*- coding: utf-8 -*-
from binascii import a2b_hex
from struct import pack
import os
from optparse import OptionParser
from gevent import monkey; monkey.patch_all()
from gevent.server import StreamServer
import csv

cert = os.path.join(os.path.dirname(__file__), 'server.crt')
key = os.path.join(os.path.dirname(__file__), 'server.key')
results = []


def response_by_token(token, timestamp):
    token_bin = a2b_hex(token)
    token_length_bin = pack('>H', (len(token_bin)))
    date = pack('>I', timestamp)
    return date + token_length_bin + token_bin


def handle(socket, address):
    print 'New connection from %s:%s' % address

    for token in results:
        socket.sendall(response_by_token(token['token'], int(token['timestamp'])))


def main():
    parser = OptionParser()
    parser.add_option(
        "-p", "--port",
        dest="port",
        help="Server port [%default]",
        default=8081)

    parser.add_option(
        "-b", "--bind_address",
        dest="bind",
        help="Bind addreess [%default]",
        default="0.0.0.0")

    parser.add_option(
        "-r", "--results_file",
        dest="rfile",
        help="Results file [%default]",
        default="results.csv")

    (options, args) = parser.parse_args()

    # By default server outputs ok responses, but a results file could be defined to define responses.
    if os.path.exists(options.rfile):
        print 'Loaded %s file' % options.rfile
        global results
        with open(options.rfile, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            results = [{'token': row[0], 'timestamp': row[1]} for row in reader]
    else:
        print 'No results file loaded, sever will accept connections but no feedback will be sended'

    print "Starting server on %s:%s" % (options.bind, int(options.port))
    StreamServer((options.bind, int(options.port)), handle, keyfile=key, certfile=cert).serve_forever()

if __name__ == "__main__":
    main()

python-gcm-dummy
======================
Dummy server that simulates apple APNS feedback service, it is designed to easy make an integration test in order to verify if tokens are
properly managed 


Responses
-------------
By default server will output ok responses but a results file can be defined.

Example file:
```
0123456780123456780123456780123456780123456780001234567812345678, 1419406068
0123456780123456780123456780123456780123456780001234567812345679, 1419405068
```

Server will automatically load any resuts.csv file in the working dir.

Usage
--------------
```
$ python2.7 server.py -r exampleresults.csv                                                                     
Loaded exampleresults.csv file
Starting server on 0.0.0.0:8081
```

Options
--------------
```
python server.py --help
Usage: server.py [options]

Options:
  -h, --help            show this help message and exit
  -p PORT, --port=PORT  Server port [8081]
  -b BIND, --bind_address=BIND
                        Bind addreess [0.0.0.0]
  -r RFILE, --results_file=RFILE
                        Results file [results.csv]
```


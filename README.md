# restful-webservice-sample
restful web service with Flask

reference: https://flask-restful.readthedocs.io/en/latest/quickstart.html

Run the service:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 197-645-399
127.0.0.1 - - [12/Nov/2017 01:12:01] "POST /library/api/v1.0/books HTTP/1.1" 201 -
127.0.0.1 - - [12/Nov/2017 01:13:07] "GET /library/api/v1.0/books HTTP/1.1" 200 -
```


GET all books
```
curl -i http://localhost:5000/library/api/v1.0/books
```

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 449
Server: Werkzeug/0.12.2 Python/3.5.2
Date: Sat, 11 Nov 2017 23:45:30 GMT

{
    "3": {
        "cover": "Paperback",
        "title": "Thinking in Systems",
        "author": "Donella H. Meadows"
    },
    "2": {
        "cover": "Paperback",
        "title": "Goedel, Escher, Bach: An Eternal Golden Braid",
        "author": "Douglas Hofstadter"
    },
    "1": {
        "cover": "Hardcover",
        "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
        "author": "Eric Evans"
    }
}
```


GET one book
```
curl -i http://localhost:5000/library/api/v1.0/book/1
```

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 169
Server: Werkzeug/0.12.2 Python/3.5.2
Date: Sat, 11 Nov 2017 23:39:54 GMT

{
    "1": {
        "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
        "cover": "Hardcover",
        "author": "Eric Evans"
    }
}
```

DELETE one book
```
curl http://localhost:5000/library/api/v1.0/book/2 -X DELETE -v
```

```
* Connected to localhost (127.0.0.1) port 5000 (#0)
> DELETE /library/api/v1.0/book/2 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.55.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.12.2 Python/3.5.2
< Date: Sat, 11 Nov 2017 23:44:07 GMT
<
* Closing connection 0
```

UPDATE one book
```
curl --header "Content-Type: application/json" --request PUT --data '{"title":"Options, Futures and other derivatives","author":"John Hull","cover":"PaperBack"}' http://localhost:5000/library/api/v1.0/book/3 -X PUT -v
```

```
* Connected to localhost (127.0.0.1) port 5000 (#0)
> PUT /library/api/v1.0/book/3 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.55.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 91
>
* upload completely sent off: 91 out of 91 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 111
< Server: Werkzeug/0.12.2 Python/3.5.2
< Date: Sun, 12 Nov 2017 00:01:27 GMT
<
{
    "cover": "PaperBack",
    "title": "Options, Futures and other derivatives",
    "author": "John Hull"
}
* Closing connection 0
```

CREATE a new book
```
curl --header "Content-Type: application/json" --request POST --data '{"title":"Les miserables","author":"Victor Hugo","cover":"PaperBack"}' http://localhost:5000/library/api/v1.0/books -v
```

```
Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /library/api/v1.0/books HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.55.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 69
>
* upload completely sent off: 69 out of 69 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 89
< Server: Werkzeug/0.12.2 Python/3.5.2
< Date: Sun, 12 Nov 2017 00:12:01 GMT
<
{
    "cover": "PaperBack",
    "title": "Les miserables",
    "author": "Victor Hugo"
}
* Closing connection 0
```
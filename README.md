# DNS to DNS over TLS proxy

## What is this?
It's a proxy which accepts DNS requests and proxy it to Cloudflare DNS server running with DNS over TLS implementation.


## Installation

1. Build the Docker image:

```
docker build -t dnstlsproxy .
```

2. Run the container:

```
docker run -p 8888:8888/tcp dnstlsproxy
```

For testing purposes it is bound to port 8888 by default, it can be published on any other port if desired.

For local testing:

```
docker run --network="host" dnstlsproxy
```

Then it can be tested with a query to localhost:8888 nameserver


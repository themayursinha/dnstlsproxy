# DNS to DNS over TLS proxy

## Implementation

Listens for DNS queries on port 8888/TCP and proxies them to Cloudfare's 1.0.0.1 nameserver through DNS over TLS, then sends the response back to the client.

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


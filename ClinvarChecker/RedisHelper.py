import redis


def connect(host, port):
    host_link = "0.0.0.0"
    port = "6379"

    r = redis.Redis(
        host=host,
        port=port,
        password="123456"
    )

    return r

def is_changed(r_host, c_id, desc):
    pass

def insert(r_host, c_id, desc):
    pass

    

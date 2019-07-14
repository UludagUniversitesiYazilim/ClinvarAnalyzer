import redis


def connect(host, port):
    host_link = "0.0.0.0"
    port = "6379"

    r = redis.Redis(
        host=host,
        port=port
    )

    return r


def add_variant(redis_host, v_id, desc, on_change, on_new_variant):
    changed = __check_if_changed(redis_host, v_id, desc)

    if changed[0] == True:
        on_change(v_id, changed[1])
        redis_host.set(v_id, desc)
        return True
    elif changed[0] == False:
        return False
    elif changed[0] == None:
        on_new_variant(v_id, changed[1])
        redis_host.set(v_id, desc)
        return True
    

def __check_if_changed(redis_host, v_id, desc):
    result = redis_host.get(v_id)
    dcmp = bytes(desc, 'utf-8')
    

    if result == dcmp:
        return False, result
    elif result == None:
        return None, None
    elif result != dcmp:
        return True, result



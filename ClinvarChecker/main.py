import ReleaseParser as parser
import RedisHelper as redis

redis_server = redis.connect(host='localhost', port=6379)

release_set = parser.get_CVset("./mock/MockData-2.xml", 0)

for i, j in release_set:
    redis.add_variant(redis_server,
                      i, j,
                      lambda x, y : print(f"Degisim: {x} - {j} (Eski:{y})"),
                      lambda x, y : print(f"Eklenen: {x} - {j}")
    )

print("done")

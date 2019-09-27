from rediscluster import RedisCluster


if __name__ == '__main__':
    start_nodes = [{"host":"192.168.208.3", "port":"7001"},
                   {"host":"192.168.208.3", "port":"7002"},
                   {"host":"192.168.208.4", "port":"7001"}
    ]
    try:
        rc = RedisCluster(startup_nodes=start_nodes, decode_responses=True)
        rc.set("foo","bar")
        print(rc.get("foo"))
    except Exception as e:
        print(e)


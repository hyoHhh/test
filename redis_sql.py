# -*- coding: utf-8 -*-
import redis

# nosql : mongodb  redis       hbase hadoop         cassandra hadoop

# redis 支持网络，可基于内存也可以持久化的日志型

# 事物 一组sql操作，要么都成功，要么都失败

# key value,数据的持久化，内存数据存在磁盘中，重启的时候再次加载

# 相当于缓存

# 原子性没有抢资源的弊端

#  性能高，支持类型多，原子性，丰富的特性，通知，过期，key，publish

# session共享，购物车

#  内存型数据库，放在内存中的

from redis import *

st=StrictRedis(host="192.168.0.104",port=6379,db=0)
print('ubuntu',st.get("ubuntu"))
print('linux',st.get("linux"))
print('linux1',st.get("linux1"))
print('linux2',st.get("linux2"))
print('linux3',st.get("linux3"))


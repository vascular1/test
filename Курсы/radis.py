import redis, os
r_server = redis.Redis(host=os.getenv("IP", "0.0.0.0"), port=6379) 
print  r_server.get('mykey')
#r_server.set('counter', 100)
r_server.incr('counter')
print 'counter: '+ r_server.get('counter') 
print r_server.lrange('my_list', 0, -1)
print r_server.lrange('my_list',0,1)

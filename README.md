## SNIPPETS

In case of problems with instances from replica set , stop MongoDB Service and run command again

mongod --port 27017 --dbpath "C:\Program Files\MongoDB\Server\6.0\data\db0" --replSet gami_note_replicaset
mongod --port 27018 --dbpath "C:\Program Files\MongoDB\Server\6.0\data\db1" --replSet gami_note_replicaset
mongod --port 27019 --dbpath "C:\Program Files\MongoDB\Server\6.0\data\db2" --replSet gami_note_replicaset

## STANDARD API

1. PATCH:
   1. It was used IETF Json Patch standard. In this case was implemented with python json patch lib.
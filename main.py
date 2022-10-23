from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from api.resources.public_shared_topic.PublicSharedTopicResource import PublicSharedTopicResource
from api.resources.shared_topic.SharedTopicListResource import SharedTopicListResource
from api.resources.shared_topic.SharedTopicResource import SharedTopicResource
from api.resources.note.NoteListResource import NoteListResource
from api.resources.note.NoteResource import NoteResource
from api.resources.topic.TopicResource import TopicResource
from api.resources.topic.TopicListResource import TopicListResource
from api.resources.topic.TopicWithNotesResource import TopicWithNotesResource
from api.resources.user.UserListResource import UserListResource
from api.resources.user.UserResource import UserResource
from config.extensions import mongo
from config.flask_mongo_sessions import MongoDBSessionInterface
from flask_cors import CORS

from config.server_config import server_config

app = Flask(__name__)
CORS(app)

api = Api(app,prefix="/gami-notes/api/v1")

app.config["MONGO_URI"] = "mongodb://jesus:123@127.0.0.1:27017/gami_notes?authSource=admin&replicaSet=%s" % \
                          server_config["replica_set_mongo"]
app.config["SWAGGER"] = {
    'title': 'Flask API Starter Kit'
}

swagger = Swagger(app)
mongo.init_app(app)

with app.app_context():
    app.session_interface = MongoDBSessionInterface(app=app,db=mongo.db,collection_name="sessions")

api.add_resource(TopicListResource,"/topics")
api.add_resource(TopicResource,"/topics/<topic_id>")
api.add_resource(TopicWithNotesResource,"/topics/<topic_id>/notes")

api.add_resource(UserListResource,"/users")
api.add_resource(UserResource,"/users/<user_id>")

api.add_resource(NoteListResource,"/notes")
api.add_resource(NoteResource,"/notes/<note_id>")

api.add_resource(SharedTopicListResource,"/shared/topics")
api.add_resource(SharedTopicResource,"/shared/topics/<topic_id>")

api.add_resource(PublicSharedTopicResource,"/public/topics/shared/<shared_topic_id>")

if __name__ == '__main__':
    app.run()

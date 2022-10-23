from bson import ObjectId


class TopicCreate(object):
    title: str
    description: str
    user_id: ObjectId

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = ObjectId(user_id)
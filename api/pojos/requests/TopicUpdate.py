from bson import ObjectId


class TopicUpdate(object):
    title: str
    description: str

    def __init__(self, title, description):
        self.title = title
        self.description = description
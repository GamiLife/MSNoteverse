class SharedTopicCreate(object):
    topic_id: str
    user_id: str

    def __init__(self, topic_id, user_id):
        self.topic_id = topic_id
        self.user_id = user_id
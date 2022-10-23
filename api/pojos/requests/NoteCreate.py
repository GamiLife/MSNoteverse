from bson import ObjectId


class NoteCreate(object):
    title: str
    description: str
    is_liked: bool
    topic_id: ObjectId
    is_memorized: bool
    is_ignored: bool

    def __init__(self, title, description, is_liked, topic_id, is_memorized, is_ignored):
        self.title = title
        self.description = description
        self.is_liked = is_liked
        self.topic_id = ObjectId(topic_id)
        self.is_memorized = is_memorized
        self.is_ignored = is_ignored
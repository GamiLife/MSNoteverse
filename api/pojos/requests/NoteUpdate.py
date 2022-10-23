from bson import ObjectId


class NoteUpdate(object):
    title: str
    description: str
    is_liked: bool
    is_memorized: bool
    is_ignored: bool

    def __init__(self, title, description, is_liked, is_memorized, is_ignored):
        self.title = title
        self.description = description
        self.is_liked = is_liked
        self.is_memorized = is_memorized
        self.is_ignored = is_ignored
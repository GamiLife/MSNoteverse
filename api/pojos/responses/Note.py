class Note:
    __id: str
    _title: str
    _description: str
    _is_liked: bool
    _is_memorized: bool
    _is_ignored: bool
    _topic_id: bool

    @property
    def _id(self):
        return self._id

    @_id.setter
    def _id(self, note_id):
        self.__id = note_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def is_liked(self):
        return self._is_liked

    @is_liked.setter
    def is_liked(self, is_liked):
        self._is_liked = is_liked

    @property
    def is_memorized(self):
        return self._is_memorized

    @is_memorized.setter
    def is_memorized(self, is_memorized):
        self._is_memorized = is_memorized

    @property
    def is_ignored(self):
        return self._is_ignored

    @is_ignored.setter
    def is_ignored(self, is_ignored):
        self._is_ignored = is_ignored

    @property
    def topic_id(self):
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        self._topic_id = topic_id
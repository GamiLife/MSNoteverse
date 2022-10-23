from api.pojos.responses.Note import Note


class TopicWithNotes:
    total_notes: int
    total_memorized: int
    notes: list[Note]

    def __init__(self,total_notes,total_memorized,notes):
        self.total_notes = total_notes
        self.total_memorized = total_memorized
        self.notes = notes

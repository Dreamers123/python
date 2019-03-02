from note_object import Note

class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))
    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
         note.memo = memo
         return True
         return False

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        return [note for note in self.notes if
                note.match(filter)]

'''n = Notebook()
n.new_note("hello world")
n.new_note("hello again")
print(n.notes[1].memo)
n.modify_memo(1,"Hi,world")
print(n.notes[1].)'''

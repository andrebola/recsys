class Artist2ArtistMixin():
    def recommend(self, artists_id=None):
        ''''Receives a list of artists ids and returns a list of Artists ids'''
        pass
class Artist2RecordingMixin():
    def recommend(self, artists_id=None):
        ''''Receives a list of artists ids and returns a list of Recordings ids'''
        pass
class Recording2RecordingMixin():
    def recommend(self, recordings_id=None):
        ''''Receives a list of recordings ids and returns a list of Recordigns ids'''
        pass
class Recording2ArtistMixin():
    def recommend(self, recordings_id=None):
        ''''Receives a list of recordings ids and returns a list of Artists ids'''
        pass
class User2SecordingMixin():
    def recommend(self, user_id=None):
        ''''Receives user id and returns a list of Recordings ids'''
        pass

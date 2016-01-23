class Artist2ArtistMixin():
    def recommend_a2a(self, artists_id=None):
        ''''Receives a list of artists ids and returns a list of Artists ids'''
        pass
class Artist2RecordingMixin():
    def recommend_a2r(self, artists_id=None):
        ''''Receives a list of artists ids and returns a list of Recordings ids'''
        pass
class Recording2RecordingMixin():
    def recommend_r2r(self, recordings_id=None):
        ''''Receives a list of recordings ids and returns a list of Recordigns ids'''
        pass
class Recording2ArtistMixin():
    def recommend_r2a(self, recordings_id=None):
        ''''Receives a list of recordings ids and returns a list of Artists ids'''
        pass
class User2RecordingMixin():
    def recommend_u2r(self, user_id=None):
        ''''Receives user id and returns a list of Recordings ids'''
        pass

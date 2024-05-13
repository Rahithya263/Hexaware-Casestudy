class Artwork:
    def __init__(self, title, description, creation_date, medium, image_url, artist_id, artwork_id=None):
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.medium = medium
        self.image_url = image_url
        self.artist_id = artist_id
        self.artwork_id = artwork_id

    # Getters and setters for artwork_id
    def get_artwork_id(self):
        return self.artwork_id

    def set_artwork_id(self, artwork_id):
        self.artwork_id = artwork_id

    # Getters and setters for artist_id
    def get_artist_id(self):
        return self.artist_id

    def set_artist_id(self, artist_id):
        self.artist_id = artist_id

    # Other getters and setters...

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_creation_date(self):
        return self.creation_date

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

    def get_medium(self):
        return self.medium

    def set_medium(self, medium):
        self.medium = medium

    def get_image_url(self):
        return self.image_url

    def set_image_url(self, image_url):
        self.image_url = image_url

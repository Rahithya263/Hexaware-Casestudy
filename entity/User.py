class User:
    def __init__(self, username, password, email, first_name, last_name, date_of_birth, favorite_artworks=None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.favorite_artworks = favorite_artworks if favorite_artworks is not None else set()
        # Getter and setter methods for other attributes...

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id
    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def add_favorite_artwork(self, artwork_id):
        self.favorite_artworks.add(artwork_id)

    def remove_favorite_artwork(self, artwork_id):
        self.favorite_artworks.discard(artwork_id)

    def get_favorite_artworks(self):
        return self.favorite_artworks

    def set_favorite_artworks(self, favorite_artworks):
        self.favorite_artworks = favorite_artworks

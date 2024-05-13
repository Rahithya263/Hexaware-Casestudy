class Gallery:
    def __init__(self, name, description, location, curator, opening_hours, gallery_id=None):
        self.__name = name
        self.__description = description
        self.__location = location
        self.__curator = curator
        self.__opening_hours = opening_hours
        self.__gallery_id = gallery_id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_location(self):
        return self.__location

    def get_curator(self):
        return self.__curator

    def get_opening_hours(self):
        return self.__opening_hours

    def get_gallery_id(self):
        return self.__gallery_id

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_location(self, location):
        self.__location = location

    def set_curator(self, curator):
        self.__curator = curator

    def set_opening_hours(self, opening_hours):
        self.__opening_hours = opening_hours

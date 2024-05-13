class ArtworkNotFoundException(Exception):
    def __init__(self,msg="Artwork not found in the database"):
        self.msg=msg
        super().__init__(self.msg)


class UserNotFoundException(Exception):
    def __init__(self,msg="User not found in the database"):
        self.msg=msg
        super().__init__(self.msg)


class ArtistNotFoundException:
    def __init__(self, msg="Artist not found in the database"):
        self.msg = msg
        super().__init__(self.msg)
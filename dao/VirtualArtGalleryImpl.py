from dao.IVirtualArtGallery import IVirtualArtGallery
from entity.Artwork import Artwork
from entity.Gallery import Gallery
from exception.myexceptions import ArtworkNotFoundException
from util.dbConnection import DBConnection
from entity.User import User
from entity.Artist import Artist
from exception.myexceptions import UserNotFoundException, ArtistNotFoundException


class VirtualArtGalleryImpl(IVirtualArtGallery):
    def __init__(self):
        self.connection = DBConnection.getconnection()

        self.users = {}  # Dictionary to store users

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID) VALUES (%s, %s, "
                "%s, %s, %s, %s)",
                (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(),
                 artwork.get_medium(), artwork.get_image_url(), artwork.get_artist_id()))

            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error adding artwork: {e}")
            return False

    def update_artwork(self, artwork: Artwork) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE Artwork SET Title = %s, Description = %s, CreationDate = %s, Medium = %s, ImageURL = %s WHERE ArtworkID = %s",
                (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(),
                 artwork.get_medium(), artwork.get_image_url(), artwork.get_artwork_id()))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating artwork: {e}")
            return False

    def remove_artwork(self, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Artwork WHERE ArtworkID = %s", (artwork_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error removing artwork: {e}")
            return False

    def search_artworks(self, keyword: str) -> list[Artwork]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Artwork WHERE LOWER(Title) LIKE %s OR LOWER(Description) LIKE %s",
                           (f"%{keyword.lower()}%", f"%{keyword.lower()}%"))
            artworks_data = cursor.fetchall()
            cursor.close()
            artworks = [Artwork(*artwork_data) for artwork_data in artworks_data]

            return artworks
        except Exception as e:
            print(f"Error searching artworks: {e}")
            return []

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT FavoriteArtworks FROM User WHERE UserID = %s", (user_id,))
            favorite_artworks_row = cursor.fetchone()
            if favorite_artworks_row:
                favorite_artworks = favorite_artworks_row[0]
                if favorite_artworks:
                    favorite_artworks += f",{artwork_id}"
                else:
                    favorite_artworks = str(artwork_id)
                cursor.execute("UPDATE User SET FavoriteArtworks = %s WHERE UserID = %s", (favorite_artworks, user_id))
            else:
                cursor.execute("INSERT INTO User (UserID, FavoriteArtworks) VALUES (%s, %s)",
                               (user_id, str(artwork_id)))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error adding artwork to favorites: {e}")
            return False

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT FavoriteArtworks FROM User WHERE UserID = %s", (user_id,))
            favorite_artworks_row = cursor.fetchone()
            if favorite_artworks_row:
                favorite_artworks = favorite_artworks_row[0]
                if favorite_artworks:
                    favorite_artwork_ids = favorite_artworks.split(",")
                    if str(artwork_id) in favorite_artwork_ids:
                        favorite_artwork_ids.remove(str(artwork_id))
                        favorite_artworks = ",".join(favorite_artwork_ids)
                        cursor.execute("UPDATE User SET FavoriteArtworks = %s WHERE UserID = %s",
                                       (favorite_artworks, user_id))
                        self.connection.commit()
                        cursor.close()
                        return True
                return False
            else:
                return False
        except Exception as e:
            print(f"Error removing artwork from favorites: {e}")
            return False

    def get_user_favorite_artworks(self, user_id: int) -> list[int]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT FavoriteArtworks FROM User WHERE UserID = %s", (user_id,))
            favorite_artworks = cursor.fetchone()[0]
            cursor.close()
            if favorite_artworks:
                return [int(artwork_id) for artwork_id in favorite_artworks.split(",")]
            else:
                return []
        except Exception as e:
            print(f"Error getting user favorite artworks: {e}")

    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = %s", (artwork_id,))
            artwork_data = cursor.fetchone()
            cursor.close()
            if artwork_data:
                # Create Artwork object
                artwork = Artwork(*artwork_data)
                return artwork
            else:
                raise ArtworkNotFoundException()
        except ArtworkNotFoundException as e:
            print(f"Error getting artwork by ID: {e}")
            return None

    def create_gallery(self, gallery: Gallery) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Gallery (Name, Description, Location, Curator, OpeningHours) VALUES (%s, %s, %s, %s, %s)",
                (gallery.get_name(), gallery.get_description(), gallery.get_location(),
                 gallery.get_curator(), gallery.get_opening_hours()))

            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error adding Gallery: {e}")
            return False

    def update_gallery(self, gallery: Gallery) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE Gallery SET Name = %s, Description = %s, Location = %s, Curator = %s, OpeningHours = %s WHERE GalleryID = %s",
                (gallery.get_name(), gallery.get_description(), gallery.get_location(),
                 gallery.get_curator(), gallery.get_opening_hours(), gallery.get_gallery_id()))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating gallery: {e}")
            return False

    def remove_gallery(self, gallery_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Gallery WHERE GalleryID = %s", (gallery_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error removing gallery: {e}")
            return False

    def get_gallery_by_id(self, gallery_id: int, gallery_data=None) -> Gallery | None:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Gallery WHERE GalleryID = %s", (gallery_id,))
            gallery_data = cursor.fetchone()
            cursor.close()
            if gallery_data:
                # Create Gallery object
                gallery = Gallery(*gallery_data)
                return gallery
            else:
                return None
        except Exception as e:
            print(f"Error getting gallery by ID: {e}")
            return None

    def search_galleries(self, keyword: str) -> list[Gallery]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Gallery WHERE LOWER(Name) LIKE %s OR LOWER(Description) LIKE %s",
                           (f"%{keyword.lower()}%", f"%{keyword.lower()}%"))
            galleries_data = cursor.fetchall()
            cursor.close()
            galleries = [Gallery(*gallery_data) for gallery_data in galleries_data]
            return galleries
        except Exception as e:
            print(f"Error searching galleries: {e}")
            return []

    def add_user(self, user: User) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO User (Username, Password, Email, FirstName, LastName, DateOfBirth, FavoriteArtworks) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (user.username, user.password, user.email, user.first_name, user.last_name, user.date_of_birth,
                 ','.join(map(str, user.favorite_artworks))))  # Convert list to comma-separated string
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False

    def update_user(self, user: User) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE User SET Username = %s, Password = %s, Email = %s, FirstName = %s, LastName = %s, DateOfBirth = %s, FavoriteArtworks = %s WHERE UserID = %s",
                (user.username, user.password, user.email, user.first_name, user.last_name, user.date_of_birth, user.favorite_artworks, user.user_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def remove_user(self, user_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM User WHERE UserID = %s", (user_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error removing user: {e}")
            return False

    def get_user_by_id(self, user_id: int) -> User:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Username, Password, Email, FirstName, LastName, DateOfBirth, FavoriteArtworks FROM User WHERE UserID = %s", (user_id,))

            user_data = cursor.fetchone()
            cursor.close()
            if user_data:
                return User(*user_data)
            else:
                raise UserNotFoundException()
        except UserNotFoundException as e:
            print(f"Error getting user by ID: {e}")
            return None

    def search_users(self, keyword: str) -> list[User]:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT * FROM User WHERE LOWER(Username) LIKE %s OR LOWER(Email) LIKE %s OR LOWER(FirstName) LIKE %s OR LOWER(LastName) LIKE %s",
                (f"%{keyword.lower()}%", f"%{keyword.lower()}%", f"%{keyword.lower()}%", f"%{keyword.lower()}%"))
            users_data = cursor.fetchall()
            cursor.close()
            users = [User(*user_data) for user_data in users_data]
            return users
        except Exception as e:
            print(f"Error searching users: {e}")
            return []

    # Methods for Artist table

    def add_artist(self, artist: Artist) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website, ContactInformation) VALUES (%s, %s, %s, %s, %s, %s)",
                (artist.name, artist.biography, artist.birth_date, artist.nationality, artist.website,
                 artist.contact_information))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error adding artist: {e}")
            return False

    def update_artist(self, artist: Artist) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE Artist SET Name = %s, Biography = %s, BirthDate = %s, Nationality = %s, Website = %s, ContactInformation = %s WHERE ArtistID = %s",
                (artist.name, artist.biography, artist.birth_date, artist.nationality, artist.website,
                 artist.contact_information, artist.artist_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating artist: {e}")
            return False

    def remove_artist(self, artist_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Artist WHERE ArtistID = %s", (artist_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error removing artist: {e}")
            return False

    def get_artist_by_id(self, artist_id: int) -> Artist | None:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Artist WHERE ArtistID = %s", (artist_id,))
            artist_data = cursor.fetchone()
            cursor.close()
            if artist_data:
                return Artist(*artist_data)
            else:
                raise ArtistNotFoundException()
        except ArtistNotFoundException as e:
            print(f"Error getting artist by ID: {e}")
            return None

    def search_artists(self, keyword: str) -> list[Artist]:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT * FROM Artist WHERE LOWER(Name) LIKE %s OR LOWER(Biography) LIKE %s OR LOWER(Nationality) LIKE %s",
                (f"%{keyword.lower()}%", f"%{keyword.lower()}%", f"%{keyword.lower()}%"))
            artists_data = cursor.fetchall()
            cursor.close()
            artists = [Artist(*artist_data) for artist_data in artists_data]
            return artists
        except Exception as e:
            print(f"Error searching artists: {e}")
            return []
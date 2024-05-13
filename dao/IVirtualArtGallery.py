from abc import ABC, abstractmethod

from entity import User, Artist
from entity.Artwork import Artwork


class IVirtualArtGallery(ABC):
    @abstractmethod
    def add_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def update_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def remove_artwork(self, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        pass

    @abstractmethod
    def search_artworks(self, keyword: str) -> list[Artwork]:
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id: int) -> list[int]:
        pass


    @abstractmethod
    def add_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def update_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def remove_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def search_users(self, keyword: str) -> list[User]:
        pass

    @abstractmethod
    def add_artist(self, artist: Artist) -> bool:
        pass

    @abstractmethod
    def update_artist(self, artist: Artist) -> bool:
        pass

    @abstractmethod
    def remove_artist(self, artist_id: int) -> bool:
        pass

    @abstractmethod
    def get_artist_by_id(self, artist_id: int) -> Artist:
        pass

    @abstractmethod
    def search_artists(self, keyword: str) -> list[Artist]:
        pass

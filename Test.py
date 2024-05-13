import unittest
from entity.Artwork import Artwork
from entity.Gallery import Gallery
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl


class TestArtworkManagement(unittest.TestCase):
    def setUp(self):
        self.virtual_art_gallery = VirtualArtGalleryImpl()

    def test_upload_new_artwork(self):
        artwork = Artwork("Test Artwork", "Test Description", "2024-05-11", "Test Medium", "test_image.jpg", 1)
        result = self.virtual_art_gallery.add_artwork(artwork)
        self.assertTrue(result)

    def test_update_artwork_details(self):
        artwork = Artwork("Test Artwork", "Test Description", "2024-05-11", "Test Medium", "test_image.jpg", 1)
        result = self.virtual_art_gallery.update_artwork(artwork)
        self.assertTrue(result)

    def test_remove_artwork(self):
        artwork_id = 1  # Provide an existing artwork ID for testing
        result = self.virtual_art_gallery.remove_artwork(artwork_id)
        self.assertTrue(result)

    def test_search_artworks(self):
        keyword = "Test"  # Provide a keyword for testing
        result = self.virtual_art_gallery.search_artworks(keyword)
        self.assertIsNotNone(result)


class TestGalleryManagement(unittest.TestCase):
    def setUp(self):
        self.virtual_art_gallery = VirtualArtGalleryImpl()

    def test_create_new_gallery(self):
        gallery = Gallery("Test Gallery", "Test Description", "Test Location", 1,
                          "Test Opening Hours")  # Assuming curator ID is 1
        result = self.virtual_art_gallery.create_gallery(gallery)
        self.assertTrue(result)

    def test_update_gallery_info(self):
        gallery = Gallery("Test Gallery", "Test Description", "Test Location", 1,
                          "Test Opening Hours")  # Assuming curator ID is 1
        result = self.virtual_art_gallery.update_gallery(gallery)
        self.assertTrue(result)

    def test_remove_gallery(self):
        gallery_id = 1  # Provide an existing gallery ID for testing
        result = self.virtual_art_gallery.remove_gallery(gallery_id)
        self.assertTrue(result)

    def test_search_galleries(self):
        keyword = "Test"  # Provide a keyword for testing
        result = self.virtual_art_gallery.search_galleries(keyword)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()




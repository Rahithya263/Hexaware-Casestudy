from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.Artwork import Artwork
from exception.myexceptions import ArtworkNotFoundException, UserNotFoundException, ArtistNotFoundException

from entity.Gallery import Gallery
from entity.User import User
from entity.Artist import Artist


def main():
    gallery_service = VirtualArtGalleryImpl()

    while True:
        print("\n1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. Search Artworks")
        print("5. Add Artwork to Favorites")
        print("6. Remove Artwork from Favorites")
        print("7. Get User Favorite Artworks")
        print("8. Get Artwork by ID")
        print("9. Create Gallery")
        print("10. Update Gallery")
        print("11. Remove Gallery")
        print("12. Search Galleries")
        print("13. Add User")
        print("14. Update User")
        print("15. Remove User")
        print("16. Get User by ID")
        print("17. Add Artist")
        print("18. Update Artist")
        print("19. Remove Artist")
        print("20. Get Artist by ID")
        print("21. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_artwork(gallery_service)
        elif choice == "2":
            update_artwork(gallery_service)
        elif choice == "3":
            remove_artwork(gallery_service)
        elif choice == "4":
            search_artworks(gallery_service)
        elif choice == "5":
            add_artwork_to_favorite(gallery_service)
        elif choice == "6":
            remove_artwork_from_favorite(gallery_service)
        elif choice == "7":
            get_user_favorite_artworks(gallery_service)
        elif choice == "8":
            artwork_id = int(input("Enter artwork ID to retrieve: "))
            try:
                artwork = gallery_service.get_artwork_by_id(artwork_id)
                if artwork:
                    print("Artwork found:")
                    print("Title:", artwork.get_title())
                    print("Description:", artwork.get_description())
                    print("Creation Date:", artwork.get_creation_date())
                    print("Medium:", artwork.get_medium())
                    print("Image URL:", artwork.get_image_url())
                    print("Artist ID:", artwork.get_artist_id())
                else:
                    print("Artwork not found.")
            except ArtworkNotFoundException:
                print("Artwork not found.")

        elif choice == "9":
            create_gallery(gallery_service)
        elif choice == "10":
            update_gallery(gallery_service)
        elif choice == "11":
            remove_gallery(gallery_service)
        elif choice == "12":
            search_gallery(gallery_service)
        elif choice == "13":
            add_user(gallery_service)
        elif choice == "14":
            update_user(gallery_service)
        elif choice == "15":
            remove_user(gallery_service)
        elif choice == "16":
            get_user_by_id(gallery_service)
        elif choice == "17":
            add_artist(gallery_service)
        elif choice == "18":
            update_artist(gallery_service)
        elif choice == "19":
            remove_artist(gallery_service)
        elif choice == "20":
            get_artist_by_id(gallery_service)
        elif choice == "21":
            break
        else:
            print("Invalid choice. Please try again.")


def add_artwork(gallery_service):
    # Get artwork details from user input
    title = input("Enter artwork title: ")
    description = input("Enter artwork description: ")
    creation_date = input("Enter artwork creation date (YYYY-MM-DD): ")
    medium = input("Enter artwork medium: ")
    image_url = input("Enter artwork image URL: ")
    artist_id = int(input("Enter artist ID: "))

    artwork = Artwork(title=title, description=description, creation_date=creation_date, medium=medium,
                      image_url=image_url, artist_id=artist_id)  # Pass artist_id parameter

    try:
        success = gallery_service.add_artwork(artwork)
        if success:
            print("Artwork added successfully!")
        else:
            print("Failed to add artwork.")
    except Exception as e:
        print(f"Error: {e}")


def update_artwork(gallery_service):
    # Get artwork ID to update
    artwork_id = int(input("Enter artwork ID to update: "))

    try:

        artwork = gallery_service.get_artwork_by_id(artwork_id)

        if artwork:

            title = input("Enter updated artwork title: ")
            description = input("Enter updated artwork description: ")
            creation_date = input("Enter updated artwork creation date (YYYY-MM-DD): ")
            medium = input("Enter updated artwork medium: ")
            image_url = input("Enter updated artwork image URL: ")

            # Update Artwork object if it exists
            artwork.set_title(title)
            artwork.set_description(description)
            artwork.set_creation_date(creation_date)
            artwork.set_medium(medium)
            artwork.set_image_url(image_url)
            artwork.set_artwork_id(artwork_id)

            success = gallery_service.update_artwork(artwork)
            if success:
                print("Artwork updated successfully!")
            else:
                print("Failed to update artwork.")
        else:
            print("Artwork not found.")
    except ArtworkNotFoundException:
        print("Artwork not found.")


def remove_artwork(gallery_service):
    artwork_id = int(input("Enter artwork ID to remove: "))

    try:

        success = gallery_service.remove_artwork(artwork_id)
        if success:
            print("Artwork removed successfully!")
        else:
            print("Failed to remove artwork.")
    except ArtworkNotFoundException:
        print("Artwork not found.")


def search_artworks(gallery_service):
    keyword = input("Enter keyword to search artworks: ")

    try:

        artworks = gallery_service.search_artworks(keyword)
        if artworks:
            print("Search results:")
            for artwork in artworks:
                print(artwork)
        else:
            print("No artworks found.")
    except Exception as e:
        print(f"Error: {e}")


def add_artwork_to_favorite(gallery_service):
    user_id = int(input("Enter user ID: "))
    artwork_id = int(input("Enter artwork ID to add to favorites: "))

    try:
        success = gallery_service.add_artwork_to_favorite(user_id, artwork_id)
        if success:
            print("Artwork added to favorites successfully!")
        else:
            print("Failed to add artwork to favorites.")
    except Exception as e:
        print(f"Error: {e}")


def remove_artwork_from_favorite(gallery_service):
    user_id = int(input("Enter user ID: "))
    artwork_id = int(input("Enter artwork ID to remove from favorites: "))

    try:

        success = gallery_service.remove_artwork_from_favorite(user_id, artwork_id)
        if success:
            print("Artwork removed from favorites successfully!")
        else:
            print("Failed to remove artwork from favorites.")
    except Exception as e:
        print(f"Error: {e}")


def get_user_favorite_artworks(gallery_service):
    user_id = int(input("Enter user ID: "))

    try:
        favorite_artwork_ids = gallery_service.get_user_favorite_artworks(user_id)
        if favorite_artwork_ids:
            print("User favorite artworks:")
            for artwork_id in favorite_artwork_ids:
                print(artwork_id)
        else:
            print("No favorite artworks found for the user.")
    except Exception as e:
        print(f"Error: {e}")


def create_gallery(gallery_service):
    gallery_name = input("Enter gallery name: ")
    description = input("Enter gallery description: ")
    location = input("Enter gallery location: ")
    curator = input("Enter curator artist ID: ")
    opening_hours = input("Enter opening hours: ")

    gallery = Gallery(name=gallery_name, description=description, location=location, curator=curator,
                      opening_hours=opening_hours)

    try:
        success = gallery_service.create_gallery(gallery)
        if success:
            print("Gallery created successfully!")
        else:
            print("Failed to create gallery.")
    except Exception as e:
        print(f"Error: {e}")


def update_gallery(gallery_service):
    gallery_id = int(input("Enter gallery ID to update: "))

    try:
        gallery = gallery_service.get_gallery_by_id(gallery_id)

        if gallery:
            name = input("Enter updated gallery name: ")
            description = input("Enter updated gallery description: ")
            location = input("Enter updated location: ")
            curator = input("Enter updated curator ID: ")
            opening_hours = input("Enter updated hours: ")

            gallery.set_name(name)
            gallery.set_description(description)
            gallery.set_location(location)
            gallery.set_curator(curator)
            gallery.set_opening_hours(opening_hours)

            success = gallery_service.update_gallery(gallery)
            if success:
                print("Gallery updated successfully!")
            else:
                print("Failed to update gallery.")
        else:
            print("Gallery not found.")
    except Exception as e:
        print(f"Error: {e}")


def remove_gallery(gallery_service):
    gallery_id = int(input("Enter gallery ID to remove: "))

    try:
        success = gallery_service.remove_artwork(gallery_id)
        if success:
            print("gallery removed successfully!")
        else:
            print("Failed to remove gallery.")
    except ArtworkNotFoundException:
        print("gallery not found.")


def search_gallery(gallery_service):
    keyword = input("Enter keyword to search gallery: ")

    try:
        galleries = gallery_service.search_galleries(keyword)
        if galleries:
            print("Search results:")
            for gallery in galleries:
                print("Gallery ID:", gallery.get_gallery_id())
                print("Gallery Name:", gallery.get_name())
                print("Description:", gallery.get_description())
                print("Location:", gallery.get_location())
                print("Curator:", gallery.get_curator())
                print("Opening Hours:", gallery.get_opening_hours())
                print()
        else:
            print("No gallery found.")
    except Exception as e:
        print(f"Error: {e}")


def add_user(gallery_service):
    # Get user details from user input
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")

    # Get favorite artworks from user input
    favorite_artworks_input = input("Enter favorite artworks (comma-separated): ")
    favorite_artworks = favorite_artworks_input.split(',')

    # Create a User object
    user = User(username=username, password=password, email=email,
                first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                favorite_artworks=favorite_artworks)

    try:
        success = gallery_service.add_user(user)
        if success:
            print("User added successfully!")
        else:
            print("Failed to add user.")
    except Exception as e:
        print(f"Error: {e}")


# Function to update a user
def update_user(gallery_service):
    user_id = int(input("Enter user ID to update: "))
    try:
        user = gallery_service.get_user_by_id(user_id)
        if user:
            username = input("Enter updated username: ")
            email = input("Enter updated email: ")
            password = input("Enter updated password: ")

            # Update User object with new details
            user.username = username
            user.email = email
            user.password = password

            success = gallery_service.update_user(user)
            if success:
                print("User updated successfully!")
            else:
                print("Failed to update user.")
        else:
            print("User not found.")
    except UserNotFoundException:
        print("User not found.")




# Function to remove a user
def remove_user(gallery_service):
    user_id = int(input("Enter user ID to remove: "))
    try:
        success = gallery_service.remove_user(user_id)
        if success:
            print("User removed successfully!")
        else:
            print("Failed to remove user.")
    except UserNotFoundException:
        print("User not found.")


# Function to get a user by ID
def get_user_by_id(gallery_service):
    user_id = int(input("Enter user ID to retrieve: "))
    try:
        user = gallery_service.get_user_by_id(user_id)
        if user:
            print("User found:")
            print("Username:", user.get_username())
            print("Email:", user.get_email())
        else:
            print("User not found.")
    except UserNotFoundException:
        print("User not found.")


# Function to add an artist
def add_artist(gallery_service):
    # Get artist details from user input
    name = input("Enter artist name: ")
    biography = input("Enter artist biography: ")
    birth_date = input("Enter artist birth date (YYYY-MM-DD): ")
    nationality = input("Enter artist nationality: ")
    website = input("Enter artist website: ")
    contact_information = input("Enter artist contact information: ")

    # Create an Artist object
    artist = Artist(name=name, biography=biography, birth_date=birth_date,
                    nationality=nationality, website=website, contact_information=contact_information)

    try:
        success = gallery_service.add_artist(artist)
        if success:
            print("Artist added successfully!")
        else:
            print("Failed to add artist.")
    except Exception as e:
        print(f"Error: {e}")



# Function to update an artist
def update_artist(gallery_service):
    artist_id = int(input("Enter artist ID to update: "))
    try:
        artist = gallery_service.get_artist_by_id(artist_id)
        if artist:
            name = input("Enter updated artist name: ")
            bio = input("Enter updated artist biography: ")

            artist.set_name(name)
            artist.set_bio(bio)

            success = gallery_service.update_artist(artist)
            if success:
                print("Artist updated successfully!")
            else:
                print("Failed to update artist.")
        else:
            print("Artist not found.")
    except ArtistNotFoundException:
        print("Artist not found.")


# Function to remove an artist
def remove_artist(gallery_service):
    artist_id = int(input("Enter artist ID to remove: "))
    try:
        success = gallery_service.remove_artist(artist_id)
        if success:
            print("Artist removed successfully!")
        else:
            print("Failed to remove artist.")
    except ArtistNotFoundException:
        print("Artist not found.")


# Function to get an artist by ID
def get_artist_by_id(gallery_service):
    artist_id = int(input("Enter artist ID to retrieve: "))
    try:
        artist = gallery_service.get_artist_by_id(artist_id)
        if artist:
            print("Artist found:")
            print("Name:", artist.get_name())
            print("Biography:", artist.get_bio())
        else:
            print("Artist not found.")
    except ArtistNotFoundException:
        print("Artist not found.")


if __name__ == "__main__":
    main()

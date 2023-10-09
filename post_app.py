from lib.post_repository import *
from lib.user_repository import *
from lib.database_connection import DatabaseConnection

class Application():
 def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/social_network.sql")

 def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
    choice = input("Welcome to the music library manager!\n What would you like to do?\n 1 - List all albums\n 2 - List all artists\n Enter your choice: ")
    if choice == '1':
        Post_repository = PostRepository(self._connection)
        Posts = Post_repository.all()

        for post in Posts:
            print(f"{post.id}: {post.title}")
            
        
        
        
    """
    link  
    """
            
            
            
            
            
            
            
            
    elif choice == '2':
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        for artist in artists:
            print(f"{artist.id}: {artist.name}: {artist.genre}")
    
#hhhh
if __name__ == '__main__':
            app = Application()
            app.run()
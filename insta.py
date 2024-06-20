import instaloader

L = instaloader.Instaloader()

def download_instagram_profile(username):
    try:
       print(f"Download posts from {username}'s Instagram profile...")
       profile = instaloader.Profile.from_username(L.context, username)

       for post in profile.get_posts():
           L.download_post(post, target=profile.username)

       print(f"All posts from {username} have been downloaded sucessfully.")
    except instaloader.exception.ProfileNotExistsExcpetion:
       print(f"The profile {username} does not exists.")
    except instaloader.exception.PrivateProfileNotFollowedException:
       print(f"The profile {username} is private. you need to follow")
    except Exception as e:
       print(f"An error ocurred: {e}")
    
if __name__ == "__main__":
   username = input("Enter the Instagram Username:")
   download_instagram_profile(username) 

# Function to create a new YouTube video
def create_youtube_video(title, description):
    new_video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return new_video

def like(youtube_video):
    if "likes" in youtube_video:
        youtube_video["likes"] += 1
    return youtube_video

def dislike(youtube_video):
    if "dislikes" in youtube_video:
        youtube_video["dislikes"] += 1
    return youtube_video


def add_comment(youtube_video, username, comment_text):
    youtube_video["comments"][username] = comment_text
    return youtube_video
youtube_vid = create_youtube_video("how to be cool like me", "yay.")

like(youtube_vid)  
dislike(youtube_vid)  
add_comment(youtube_vid, "bla bla bla", "omgggg so goodddd")  

for i in range(494): 
    like(youtube_vid)


print(youtube_vid)

import os


def get_directory():
    directory = "/media/moloch/e17eec4d-e2e0-4b02-b41d-34338dd9ea38/Movies"
    return directory


def search_for_videos(directory):
    return (video for video in os.listdir(directory) if video.endswith(".mkv"))


def list_videos(video):
    print(video)


#def user_choice():




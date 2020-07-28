import os
import functions


def video_lister():
    directory = functions.get_directory()
    video = functions.search_for_videos(directory)
    video_listing = functions.list_videos(video)
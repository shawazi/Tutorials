from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
import time
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "D:/Downloads"
dest_dir_music = "D:/Music"
dest_dir_video = "D:/Videos"
dest_dir_image = "D:/Pictures"
dest_dir_doc = "D:/Documents"
dest_dir_other = "D:/Other"
dest_dir_torrents = "D:/Torrents"

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def makeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = makeUnique(dest, name)
        old_Name = join(dest, name)
        new_Name = join(dest, unique_name)
        rename(old_Name, new_Name)
    move(entry, dest)

class Mover(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_other_files(entry, name)
                self.check_torrent_files(entry, name)



    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                dest = dest_dir_music
                move(dest, entry, name)
                logging.info(f"Moved audio file: {name}")
    
    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                dest = dest_dir_video
                move(dest, entry, name)
                logging.info(f"Moved video file: {name}")
    
    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                dest = dest_dir_image
                move(dest, entry, name)
                logging.info(f"Moved image file: {name}")
    
    def check_document_files(self, entry, name):
        for document_extension in document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                dest = dest_dir_doc
                move(dest, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_other_files(self, entry, name):
        if not name.endswith(".torrent"):
            dest = dest_dir_other
            move(dest, entry, name)
            logging.info(f"Moved other file: {name}")
    
    def check_torrent_files(self, entry, name):
        if name.endswith(".torrent"):
            dest = dest_dir_torrents
            move(dest, entry, name)
            logging.info(f"Moved torrent file: {name}")
                


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = Mover() # create an instance of the event handler
    observer = Observer() # create an observer
    observer.schedule(event_handler, path, recursive=True) # schedule the observer to monitor the path for events
    observer.start() # start the observer
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
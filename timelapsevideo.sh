# make a video from timelapse images
ffmpeg -f image2 -pattern_type glob -framerate 10 -i 'snapshot*.jpg' -s 800x600 snapshot.avi

import glob
from PIL import Image

# get all the jpg files from the current folder
for infile in glob.glob("*.jpg"):
  im = Image.open(infile)
  # convert to thumbnail image
  im.thumbnail((400, 400), Image.ANTIALIAS)
  # don't save if thumbnail already exists
  if infile[0:5] != "thumb_":
    # prefix thumbnail file with T_
    im.save("thumb_" + infile, "JPEG", subsampling=0, quality=100)

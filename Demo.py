# import dependencies
import requests
import shutil

# build a function for reuse
def df(image_url,filename):
    # send request to get the webpage/element
	r = requests.get(image_url, stream = True) # used stream = True to Control Body Content Workflow
    # if request successfull then server send us status code 200
    # so if status code 200 then connection implemented and we're ready to progress
	if r.status_code == 200:
        # for download picture file we need to decode it, if we don't the file size would be zero!
	    r.raw.decode_content = True
        # write binary data to generate the image file
	    with open(filename,'wb') as f:
            # https://docs.python.org/3/library/shutil.html#:~:text=shutil.copyfileobj(fsrc%2C%20fdst%5B%2C%20length%5D)
	        shutil.copyfileobj(r.raw, f)
	    print('Image sucessfully Downloaded: ',filename)
    # if server send us another code that means we can't progress further
	else:
	    print('Image not retreived')

# __main__
# loop to urls and filenames that you need to download
# you can give manual generated list also to download only specific images
# here i given example using range that provide filename from 1000 to 1200 => 201 files total
# but some images in between are not available
for i in range(1000,1200+1):
	URL = f"https://sololearnuploads.azureedge.net/uploads/courses/{i}.png"
	fname = f"/content/drive/MyDrive/outputs/iconsdemo/{i}.png"
	df(URL,fname)
import urllib.request

# Set the URL of the file and the path where we want to save it
link = "https://www.example.com/test.pdf"

# Set the path to download (remember to use double backslash "\\" instead of single one)
file_path = "C:\\Users\\%USERPROFILE%\\Desktop"

# Download the file and save it in the specified path
urllib.request.urlretrieve(link, file_path)

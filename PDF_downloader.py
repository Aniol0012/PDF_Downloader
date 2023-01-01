import urllib.request

# Set the path to download (remember to use double backslash "\\" instead of single one)
file_path = ".\\"

# Example
#file_path = "C:\\Users\\YOUR_USER\\Desktop"

# Set the URL's of the files
links = [ # CHANGE THIS LINKS
    "https://www.example.com/test_1.pdf",
    "https://www.example.com/test_2.pdf",
    "https://www.example.com/test_3.pdf",
    "https://www.example.com/test_4.pdf",
    "https://www.example.com/test_5.pdf",
    "https://www.example.com/test_6.pdf",
    "https://www.example.com/test_7.pdf",
]

# Do not modify under this
file_number = 0

print("Downloading files:")

for link in links:
    file_number += 1
    print(file_number, "-", link)
    # Sets the url name of the file
    file_name = link.split("/")[-1]
    file_path_w_name = file_path + file_name
    urllib.request.urlretrieve(link, file_path_w_name)

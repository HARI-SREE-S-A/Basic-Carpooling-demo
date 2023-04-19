endpoint = "https://api.tomtom.com/map/1/staticimage"
api_key = "O2svYO9eEnF7PxMsKGjEps0oTVZnHMG4"
lat = 8.524139
lon = 76.936638
zoom = 1
width = 256
height = 256

# Define the complete URL
url = f"{endpoint}?key={api_key}&center={lat},{lon}&zoom={zoom}&width={width}&height={height}"

# Send a GET request to the API
response = requests.get(url)
print(response.headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the image in the notebook
    Image(response.content)
    
    img = plt.imread(BytesIO(response.content)) 
    plt.imshow(img)
    plt.show()
    
else:
    print("Error: Unable to retrieve map")

# Image In Roblox
Show any image in roblox.

## Warning: THIS IS NOT FOR USE IN A REAL GAME! This is for testing only.

##How it works:
When you make a request on the website, it makes a requests to the api, when the api gets the requests, it sends it to the ImageLoader, and if the Image works, it will use ImageToRobloxJson to put it into Data.json, then, when the Image in roblox updates, it will be put into roblox, this all depends on what you set your upload speed to.

## Files:

`Data.json`: Where the Data is sent for Roblox to use to make the image.

`image_cache.png`: The image used to make the image for Roblox.

`ImageLoader.py`: Loads the Image from online, into the Data.json file.

`ImageLoader.rbxm`: The model for the screen in Roblox.

`index.html`: A basic-example website for the image loader.

`Loader.lua`: The script inside the `ImageLoader.rbxm`.

`README.md`: The file your reading right now....

`Server.py`: The main server for the website.

## How to setup:
First:
Put `index.html` and `Data.json` into the `public_html` directory or a directory inside of `public_html`.

Next:
Put `ImageLoader.py`, `image_cache.png` and `Server.py` into the same directory somewhere on the server.

Next:
Put `ImageLoader.rbxm` into the Roblox Game (A test game, not a real game)

Next:
Go into `index.html`, `ImageLoader.py`, `Server.py`, and the script inside of `ImageLoader.rbxm`, and follow the comments inside.

Questions? Find a way to contact me at https://danfoodz.github.io

import requests

url = "https://background-removal.p.rapidapi.com/remove"

# payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "f9b16392f8msh88bf2970cb0c95ap1b51f5jsn5d5e18b4d434",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


# response = requests.post(url, data=payload, headers=headers)


async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST",url,  data=payload, headers=headers)
    return response.json()['response']['image_url']
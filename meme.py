from PIL import Image

image=Image.open("example.jpg")
red, green, blue = image.split()


coordinates = (100,0, image.width, image.height)
cropped = red.crop(coordinates)

left_crop = 50
right_crop = 50
width,height = image.size
new_width = width - (left_crop + right_crop)
left = left_crop
top = 0
right = left + new_width
bottom = height
cropped_image = red.crop((left, top, right, bottom))

image1=Image.blend(cropped , cropped_image, 0.5)

left_crop = 50
right_crop = 50
width,height = image.size
new_width = width - (left_crop + right_crop)
left = left_crop
top = 0
right = left + new_width
bottom = height
crop_image = blue.crop((left, top, right, bottom))

left_crop = 0
right_crop = 100
width,height = image.size
new_width = width - (left_crop + right_crop)
left = left_crop
top = 0
right = left + new_width
bottom = height
cropped_img = blue.crop((left, top, right, bottom))

image2=Image.blend(cropped_img, crop_image, 0.5)


left_crop = 50
right_crop = 50
width,height = image.size
new_width = width - (left_crop + right_crop)
left = left_crop
top = 0
right = left + new_width
bottom = height
image3 = green.crop((left, top, right, bottom))

new_image = Image.merge("RGB", (image1, image3, image2))

new_image.thumbnail ((80, 80))
new_image.save("smileface.jpg")

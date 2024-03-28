import cv2
import os 

images = os.listdir('images')

def calculate_size(scale_percentage, w, h):
  new_w = int(w * scale_percentage / 100)
  new_h = int(h * scale_percentage / 100)
  return (new_w, new_h)

def resize(image_path, scale_percentage, resized_path):
  image = cv2.imread(image_path)
  new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
  print(new_dim)
  resized_image = cv2.resize(image, new_dim)
  cv2.imwrite(resized_path, resized_image)

for image in images:
  resize(f"images/{image}", 50, f"resized_images/{image}")
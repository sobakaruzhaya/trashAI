from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("models/best.pt")


# from PIL
im1 = Image.open("0000.png")
results = model.predict(source=im1, save=True)  # save plotted images


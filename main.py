import os

from ultralytics import YOLO
import cv2

from moviepy.editor import ImageSequenceClip
import os


images_folder = "./images"


image_files = [f for f in os.listdir(images_folder) if f.endswith(".png")]


image_files.sort()


image_paths = [os.path.join(images_folder, f) for f in image_files]


clip = ImageSequenceClip(image_paths, fps=24)

# Сохраняем видео в формате mp4
clip.write_videofile("1.mp4")

VIDEOS_DIR = os.path.join('.')
video_path = os.path.join(VIDEOS_DIR, '1.mp4')
video_path_out = '{}_out1.mp4'.format(video_path)
frames_output_dir = 'frames_output'  # Create a directory to save the output files if it doesn't exist
os.makedirs(frames_output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'models', 'best.pt')

# Load a model
model = YOLO(model_path)

threshold = 0.5

frame_count = 0  # Initialize frame count
while ret:
    results = model(frame)[0]

    # Count the number of objects for each class in the frame
    class_counts = {}  # Dictionary to store counts for each class

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            class_name = results.names[int(class_id)].upper()

            if class_name not in class_counts:
                class_counts[class_name] = 0
            class_counts[class_name] += 1

            # Draw bounding boxes and labels on the frame
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, class_name, (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Write the frame with bounding boxes to the output video
    out.write(frame)

    # Save the class counts to a text file
    frame_txt = os.path.join(frames_output_dir, f"{frame_count:04d}.txt")
    with open(frame_txt, 'w') as txt_file:
        for class_name, count in class_counts.items():
            txt_file.write(f"{count}\n")

    frame_count += 1
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()

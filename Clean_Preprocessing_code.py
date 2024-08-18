import os
import random
import numpy as np
from keras.preprocessing import image

# Step 1: Download the dataset
!rm -rf Images
!wget -O dataset.zip https://www.dropbox.com/sh/2idnozs4741hzkr/AABXTlPlU-1f4L_VdS4wY06ca?dl=1
!unzip -q dataset.zip -d Images

# Step 2: Check extracted folders
folders = os.listdir("Images")
print(folders)

# Expected output: ['horses', 'humans', 'dogs', 'cats']

# Step 3: Count images in each category
for f in folders:
    path = os.path.join("Images", f)
    print(f"{f}: {len(os.listdir(path))} images")

# Step 4: Prepare image data and labels
image_data = []
labels = []
label_dict = {"cats": 0, "dogs": 1, "horses": 2, "humans": 3}

for category in folders:
    path = os.path.join("Images", category)
    for img_name in os.listdir(path):
        img = image.load_img(os.path.join(path, img_name), target_size=(224, 224))
        img_array = image.img_to_array(img)
        image_data.append(img_array)
        labels.append(label_dict[category])

print(f"Total images: {len(image_data)}, Total labels: {len(labels)}")

# Step 5: Shuffle and prepare data for training
combined = list(zip(image_data, labels))
random.shuffle(combined)
image_data[:], labels[:] = zip(*combined)

# Convert to numpy arrays
X_train = np.array(image_data)
Y_train = np.array(labels)

print(X_train.shape, Y_train.shape)
print(Y_train)

# Expected output:
# (808, 224, 224, 3) (808,)
# Array with shuffled labels

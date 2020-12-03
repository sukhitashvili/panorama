import os
import cv2


folder_path = 'images'
img_folders = os.listdir(folder_path)

for img_folder in img_folders:
    img_names = os.listdir(os.path.join(folder_path, img_folder))
    image_list = []
    for img_name in img_names:
        img_path = os.path.join(folder_path, img_folder, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (0, 0), None, 0.2, 0.2)  # resize to its 20% (images are huge)
        image_list.append(img)

    stitcher = cv2.Stitcher.create()
    status, result = stitcher.stitch(image_list)
    if status == cv2.STITCHER_OK:
        cv2.imshow(img_folder, result)
        cv2.waitKey(2000)
    else:
        print('Create panorama failed!')

cv2.waitKey(0)
cv2.destroyAllWindows()
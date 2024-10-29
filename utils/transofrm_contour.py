import cv2
import numpy as np

def parse_predictions(
                    image: np.array, 
                    contours: list, 
                    output_path: str
                ):
    image_show = image.copy()
    image_show = np.ascontiguousarray(image_show[:, :, ::-1])
    with open(output_path, 'w') as f:
        for cont in contours:
            rect = cv2.minAreaRect(cont)
            points = cv2.boxPoints(rect)
            points = np.int0(points)
            cv2.drawContours(image_show, [points], 0, (0, 255, 0), 3)
            p = np.reshape(points, -1)
            f.write('{},{},{},{},{},{},{},{}\r\n'
                    .format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
    return image_show
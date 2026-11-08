import cv2
import os


def read_image(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Ошибка: Файл '{file_path}' не найден в системе.")
    
    img = cv2.imread(file_path)

    if img is None: 
        raise ValueError(f"Ошибка: Файл '{file_path}' поврежден или не является изображением.")
    
    return img
import cv2
import os
import numpy as np
from running_string.settings import MEDIA_ROOT

# Функция для создания видео с бегущей строкой
def create_running_string(message):


    # Размеры экрана, fps, скорость перемещения строки
    width, height = 100, 100
    fps = 30
    velocity = round(0.45 * (len(message) + 1))

    # Создание пути до видеофайла
    path = os.path.join(MEDIA_ROOT, f'{message}.mp4')
    # Создание видеофайла
    result = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Пустой кадр
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Цвет фона (B, G, R)
    background_color = (140, 20, 20)

    # Начальные координаты для бегущей строки
    x, y = width, height // 2

    # Установка параметров шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1.5
    font_thickness = 2
    font_color = (255, 0, 200)  # Фиолетовый цвет текста

    # Покадровое прохождение
    for t in range(fps * 3):  # 3 секунды с частотой 30 кадр/сек

        # Заполнение кадра
        for i in range(100):
            for j in range(100):
              frame[i][j] = background_color
        

        # Шаг бегущей строки
        x -= velocity  

        # Вставка текста по координате
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        # Запись кадра
        result.write(frame)

    # Закрытие видеопотока
    result.release()

    # Возврат пути до файла
    return path
# -*- coding: utf-8 -*-

import random
from flask import Flask, jsonify

app = Flask(__name__)

# Список ссылок на картинки
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
]

@app.route("/random-image")
def random_image():
    # Генерируем случайное число для выбора случайной ссылки
    random_index = random.randint(0, len(image_urls) - 1)
    random_image_url = image_urls[random_index]
    
    # Создаем словарь с результатом
    result = {
        "image_url": random_image_url
    }
    
    # Возвращаем результат в формате JSON
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=1234)
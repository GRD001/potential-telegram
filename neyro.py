import tensorflow as tf
import numpy as np

# Создаем список уведомлений
notifications = [
    "У вас новое сообщение!",
    "Проверьте свою электронную почту",
    "Вам необходимо подтвердить свой аккаунт",
    "Ваш заказ отправлен",
    "Вы выиграли скидку на следующую покупку",
    # Добавьте сюда остальные тексты уведомлений
]

# Создаем функцию для кодирования уведомлений в числовые векторы
def encode_notification(notification):
    return [ord(c) for c in notification]

# Создаем функцию для декодирования числовых векторов в уведомления
def decode_notification(encoded_notification):
    return ''.join([chr(int(x)) for x in encoded_notification])

# Создаем случайный вектор, который будет использоваться для генерации уведомлений
random_vector = tf.random.uniform(shape=[1, 1000])

# Создаем модель нейронной сети с одним скрытым слоем
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=100, activation='relu', input_shape=[1000]),
    tf.keras.layers.Dense(units=len(notifications), activation='softmax')
])

# Компилируем модель с категориальной кросс-энтропийной функцией потерь
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Обучаем модель на случайном векторе
model.fit(random_vector, tf.keras.utils.to_categorical(np.random.randint(len(notifications), size=1), num_classes=len(notifications)))

# Генерируем случайный вектор и предсказываем уведомление на основе него
random_vector = tf.random.uniform(shape=[1, 1000])
predicted_index = np.argmax(model.predict(random_vector))
predicted_notification = notifications[predicted_index]

# Выводим результат
print(predicted_notification)

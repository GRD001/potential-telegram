import tensorflow as tf
from tensorflow.keras import layers, models

# Загрузка и подготовка датасета MNIST
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images, test_images = train_images / 255.0, test_images / 255.0

# Создание архитектуры нейронной сети
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)), # Преобразование 2D-массива (28x28) в 1D-массив (784)
    layers.Dense(128, activation='relu'),   # Полносвязный слой с 128 нейронами и функцией активации ReLU
    layers.Dropout(0.2),                   # Dropout слой для регуляризации (отключения случайных нейронов)
    layers.Dense(10, activation='softmax')  # Выходной слой с 10 нейронами для классификации 10 классов (цифры от 0 до 9)
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение нейронной сети
model.fit(train_images, train_labels, epochs=5, batch_size=32, validation_data=(test_images, test_labels))

# Оценка точности на тестовом наборе данных
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Точность на тестовом наборе данных:", test_acc)

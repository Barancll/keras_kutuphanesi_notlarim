##MMIST Veri Kümesini Yükleme
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

##Yapay Sinir Ağı Mimarisi
from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

##Yapay Sinir Ağı(YSA) Modelinin Derlemesi
network.compile(optimizer ='rmsprop', 
                loss='categorical_crossentropy',
                metrics=['accuracy'])

##Girişlerin Ve Etiketlerin Hazırlanması
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

##YSA Modelinin Eğitilmesi
network.fit(train_images, train_labels, epochs=5, batch_size= 128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test loss:', test_loss)
print('test accuracy:', test_acc)



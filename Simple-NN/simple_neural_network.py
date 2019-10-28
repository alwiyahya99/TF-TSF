from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np
from imutils import paths
import argparse
import cv2
import os

def image_to_feature_vector(image, size=(32, 32)):
    # ubah ukuran gambar ke ukuran tetap, lalu ratakan gambar menjaadi
    # daftar intensitas piksel rendah
    return cv2.resize(image, size).flatten()

# bangun argumen parse dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input dataset")
ap.add_argument("-m", "--model", required=True,
                help="path to output model file")
args = vars(ap.parse_args())

# ambil daftar gambar yaang akan diuraikan
print("[INFO] describing images.....")
imagePaths = list(paths.list_images(args["dataset"]))

# inisialissi matriks data dan daftar label
data = []
labels = []

# ulangi masukan gambar di atas
for (i, imagePath) in enumerate(imagePaths):
    image = cv2.imread(imagePath)
    label = imagePath.split(os.path.sep)[-1].split(".")[0]
    # buat intensitas vektor piksel mentah, lalu perbarui matriks data dan daftar labels
    features = image_to_feature_vector(image)
    data.append(features)
    labels.append(label)

    # tampilkan dan perbarui setiap 1000 gambar
    if i > 0 and i % 1000 == 0 :
        print("[INFO] Procesed {}/{}".format(i, len(imagePaths)))

# mengubah label dari string ke integer
le = LabelEncoder()
labels = le.fit_transform(labels)

# skala piksel gambar input ke kisaran [0, 1], lalu ubah
# label menjadi vektor dalam kisaran [0, num_classes] - ini
# Menghasilkan vektor untuk setiap label tempat indeks label
# diatur ke `1` dan semua entri lainnya ke` 0`
data = np.array(data) / 255.0
labels = np_utils.to_categorical(labels, 2)

# mempartisi data menjadi pelatihan dan pengujian split, menggunakan 75%
# data untuk pelatihan dan 25% sisanya untuk pengujian
print("[INFO] constructing training/testing split....")
(trainData, testData, trainLabels, testLabels) = train_test_split(
    data, labels, test_size=0.25, random_state=42)

# mendefinisikan arsitekture jaringan
model = Sequential()
model.add(Dense(750, input_dim=3072, init="uniform", activation="relu"))
model.add(Dense(350, activation="relu", kernel_initializer="uniform"))
model.add(Dense(2))
model.add(Activation("softmax"))

# latih model menggunakan SGD
print("[INFO] compiling model....")
sgd = SGD(lr=0.01)
model.compile(loss="binary_crossentropy", optimizer=sgd, metrics=["accuracy"])
model.fit(trainData, trainLabels, epochs=50, batch_size=128, verbose=1)

# tampilkan nilai accuracy dari setiap testing data
print("[INFO] evaluating on testing set....")
(loss, accuracy) = model.evaluate(testData, testLabels, batch_size=128, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss, accuracy * 100))

# membuang jaringan arsitekture dan berat ke file
print("[INFO] dumping architecture and weights to file....")
model.save(args["model"])
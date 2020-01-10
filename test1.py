from __future__ import absolute_import, division, print_function, unicode_literals, unicode_literals
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)
# keras : 파이썬으로 작성된 오픈소스 신경망 라이브러리

fasion_mnist = keras.datasets.fashion_mnist # tensorflow에서 바로 load

(train_images, train_labels),(test_images, test_labels) = fasion_mnist.load_data()
# 4개의 numpy 배열 : train_image, train_label : 훈련할때 사용하는 data, test_image label : 테스트할떄 사용

class_names = ['T-shirt/top','Trouser', 'Pullover','Dress','Coat','Sandal','Shirt','Sneakers','Bag','Ankle boot']
#label이 0~9까지의 정수배열로 옷의 class를 나타냈기 때문에 ->class를 다시 이름을 붙인다.

print(train_images.shape) # 60000개 이미지 28x28 사이즈
print(len(train_labels)) # 각이미지에 대한 label 개수가 60000개
print(train_labels) # 각 이미지가 무슨 레벨을 가지고 있는지

print(test_images.shape) # test에 대해
print(len(test_labels))

# data 전처리 (preprocessing)
# plt.figure()
# plt.imshow(train_images[8]) # train image 배열중 이미지 한개를 봄
# plt.colorbar()
# plt.grid(False)
# plt.show()

train_images = train_images/255.0 # 이미지 값의 범위가 원래 0~255 이를 0~1사위 범위로 조정
test_images = test_images/255.0 # 이게 전처리 과정

# plt.figure(figsize=(10,10))
# for i in range(25): # train data set중에서 25개만
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]]) # 아래에 클래스 이름 출력
# plt.show()

# 모델은 layer로 이루어져 있다 layer가 data에서 feature를 추출한다
model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)), # 28x28 = 784 28x28 2차원 배열을 1차원 배열로(일렬로) 변환, 학습하는 가중치(parameter)는 없다
    # 데이터를 일렬로 펼친후 2개의 layer를 통과시킨다.
    keras.layers.Dense(128, activation='relu'), # dense층은 fully-connected 층, 128개의 노드를 가진다.
    keras.layers.Dense(10, activation = 'softmax') # softmax층 10개의 확률을 반환하고 반환된 값의 전체 합은 1 각 노드는 현재 이미지가 전체 10개 클래스중 어디에 속하는 지에 대한 확률을 출력
])

model.compile( # 모델 train을 하기 전 필요한 설정
    optimizer = 'adam', # 데이터와 손실함수 바탕으로 모델 업데이트 방법을 결정
    loss = 'sparse_categorical_crossentropy', # train하는 동안 모델의 오차 측정 이 함수를 최소화해야함
    metrics = ['accuracy'] # train과 test 단계를 모니터링 : 올바르게 분류된 이미지 비율인 accuracy를 이욯
)

model.fit(train_images, train_labels, epochs = 5) # train data(이미지, 라벨)를 모델에 넣음, epoch = 5
# -> 모델이 이미지와 레이블을 매핑하는 방법을 배움
# -> test set에 대한 모델예측을 만들고 이 예측이 test_label 정답과 맞는지 확인
# print("\n train over")
# accuracy평가 : test set에서 모델의 성능을 비교
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)
# print("\n test accuracy = ", test_acc)
# print("\n test loss = ", test_loss) # test set accuracy가 train보다 조금 낮다

predictions = model.predict(test_images) # train된 모델을 사용해 test이미지에 대한 예측을 만들수 있다
# print(predictions[0]) # 10개의 숫자 배열(확률)로 나타남 (각 옷 클래스에 대한 모델의 신뢰도(confidence))
ans = np.argmax(predictions[0]) # 0번째 옷 이미지에 대한 가장 높은 신뢰도를 얻은 클래스를 찾기
# print(ans)
# print(test_labels[0])

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap = plt.cm.binary)

    predicted_label = np.argmax(predictions_array)

    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel ("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                          100*np.max(predictions_array),
                                          class_names[true_label]),
                color = color)

def plot_value_array(i, predictions_array, true_label):
     predictions_array, true_label = predictions_array[i], true_label[i]
     plt.grid(False)
     plt.xticks([])
     plt.yticks([])
     thisplot = plt.bar(range(10), predictions_array, color = '#777777')
     plt.ylim([0,1])
     predicted_label = np.argmax(predictions_array)

     thisplot[predicted_label].set_color('red')
     thisplot[true_label].set_color('blue')

# 잘 예측된 레이블은 파란색으로 잘못 예측된 레이블은 빨강색으로 표현된다 (숫자는 신뢰도인데 신뢰도가 높을때도 잘못 예측할 수 있다)
# i = 12
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(i, predictions, test_labels, test_images)
# plt.subplot(1,2,2)
# plot_value_array(i, predictions, test_labels)
# plt.show()

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize = (2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels)
plt.show()

img = test_images[0] # test set에서 image하나를 선택 -> size=(28,28)
img = (np.expand_dims(img,0)) # tf.keras 모델으 한번에 이미지 묶음 (=batch)로 prediction 하는데에 최적화 되어있음 -> 1개 이미지를 사용하면 2차원 배열
print(img.shape)

predictions_single = model.predict(img)
print(predictions_single)

plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation = 45)
print(np.argmax(predictions_single[0]))
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
# !pip install -q tf-nightly-2.0-preview
import tensorflow as tf

import tensorflow_hub as hub
import tensorflow_datasets as tfds

print("version:", tf.__version__)
print('즉시 실행 모드:', tf.executing_eagerly())
print('hub version', hub.__version__)
print("GPU","available" if tf.config.experimental.list_physical_devices("GPU") else "not available")

# IMDB 데이터셋은 텐서플로 데이터셋에 포함되어있다.
# 다음 코드는 IMDB 데이터셋을 컴퓨터에 다운
train_validation_split = tfds.Split.TRAIN.subsplit([6,4]) # 훈련세트를 6:4로 나눔
(train_data, validation_data),  test_data = tfds.load(name = "imdb_reviews",
                                                      split = (train_validation_split, tfds.Split.TEST),
                                                      as_supervised = True)

# 데이터의 형태 : 전처리된 정수배열(=영화리뷰에 나오는 단어들), label은 0: 부정적 리뷰, 1: 긍정적 리뷰
train_examples_batch, train_labels_batch = next(iter(train_data.batch(10))) # 처음 10개의 샘플 출력
# print(train_examples_batch)
# print(train_labels_batch)

# 모델 구성 : 3가지 중요한 결정 필요
# 1. 어떻게 text를 표현할 것인가
# 2. 모델에서 얼마나 많은 층을 사용할 것인가
# 3. 각 층에서 얼마나 많은 hidden unit을 사용할 것인가
# input은 문장, 예측 레이블은 0 또는 1
# 텍스트를 표현하는 한 방법은 문장을 임베딩(embedding)벡터로 바꾸는 것 (:첫번째 층을 pretraining된 임베딩 모델을 사용)
# 임베딩을 하면 나온 벡터의 크기는 일정

embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(embedding, input_shape = [], dtype=tf.string, trainable = True) # 문장을 임베딩 시키기 위한 텐서플로 허브모델
hub_layer(train_examples_batch[:3]) # 입력 텍스트 길이와 상관없이 출력은 (num_examples, embedding_dimension) 크기가 된다

model = tf.keras.Sequential()
model.add(hub_layer) # 허브 층: pretrain된 모델이 1개 문장을 토큰으로 나누고 각 토큰의 임베딩을 연결하여 반환합니다.
model.add(tf.keras.layers.Dense(16, activation = 'relu')) # 16개의 hidden unit을 가진 fully connected 층
model.add(tf.keras.layers.Dense(1,activation = 'sigmoid')) # 1개의 출력노드를 가진 fully-connected 층
                                                           # 신뢰도 수준을 표현하는 0~1사이 실수가 출력됨
model.summary()

model.compile(optimizer = 'adam',
              loss = 'binary_crossentropy', # 이진 분류문제이고 모델이 확률을 출력하므로 이 로스함수 사용
                                            # 확률분포간의 거리 측정(정답인 target 분포와 예측 분포사이의 거리)
              metrics = ['accuracy'])

# 512개 샘플로 이루어진 mini-batch 에서 20 epoch동안 train
history = model.fit(train_data.shuffle(10000).batch(512),
                    epochs = 20,
                    validation_data = validation_data.batch(512),
                    verbose = 1)

# 모델 성능 확인 (accuracy와 loss)
results = model.evaluate(test_data.batch(512), verbose = 2)
for name, value in zip(model.metrics_names, results):
    print("%s: %.3f" %(name,value))
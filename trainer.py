from __future__ import print_function
import json as js
import numpy as np
import time
import os
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
import matplotlib.pyplot as plt
from encoding import encode
from encoding import decode
import json
import numpy as np

def get_longest_string(array):
    string = list(array)[0]
    for item in array:
        if len(string) < len(item):
            string = item
    return len(encode(string))


data = json.loads(open("RS-10_data.json").read())

longest_question = get_longest_string(data.keys())
longest_comment = get_longest_string(data.values())
print(longest_question)
print(longest_comment)

x_train = np.zeros((len(data.keys()), longest_question))
y_train = np.zeros((len(data.values()), longest_comment))

print("x_train shape: " + str(x_train.shape))
print("y_train shape: " + str(y_train.shape))

num_classes = longest_comment

for i,post_title in enumerate(data.keys()):
    x_train[i] = encode(post_title, padding=longest_question)

for i,comment_body in enumerate(data.values()):
    y_train[i] = encode(comment_body, padding=longest_comment)

batch_size = 2
epochs = 7

model = Sequential()

# Dense layers and output
model.add(Dense(longest_question, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,batch_size=batch_size,epochs=epochs,verbose=1)
score = model.evaluate(x_train, y_train, verbose=0)
finish_time = str(time.time())
model.save("model"+finish_time[:finish_time.find(".")]+".hf")
print('Test loss:', score[0])
print('Test accuracy:', score[1])
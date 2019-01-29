from keras.models import load_model
import numpy as np
from encoding import encode
from encoding import decode

model = load_model('Model-0.1.hf')

post_title = input("What do you want to know from u/rogersimon10? \n")
post_title = "What’s the worst thing you’ve eaten out of politeness?"
encoded_title = np.array(encode(post_title, padding=192))
encoded_title.reshape((-1))
print(encoded_title)
print(encoded_title.shape)
print(len(encoded_title))
encoded_answer = model.predict(encoded_title)
decoded_answer = decode(encoded_answer)

print(decoded_answer)
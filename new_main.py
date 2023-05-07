# importing os module 

import os
# Get the value of 'home'
# environment variable
key = 'MONGODB_URL_KEY'
value = os.getenv(key, None)
print(value)
import pickle

with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

print(type(data))
print(data)

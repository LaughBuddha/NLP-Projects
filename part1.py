from pymagnitude import *

file_path = "GoogleNews-vectors-negative300.magnitude"
vectors = Magnitude(file_path)

print(vectors.distance("cat", "dog"))
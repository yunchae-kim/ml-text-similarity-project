import numpy as np
from sentence_transformers import SentenceTransformer

# Load the input lines from input.txt
with open("/usr/local/dataset/input.txt", "r") as file:
    lines = file.readlines()

# Remove any trailing newline characters from the lines
lines = [line.strip() for line in lines]

# Load the sentence-transformers model
model = SentenceTransformer("AnnaWegmann/Style-Embedding")

# Implement batching with a batch size of 2
batch_size = 2
num_batches = len(lines) // batch_size
remaining_lines = len(lines) % batch_size

embeddings = []
for i in range(num_batches):
    batch_lines = lines[i * batch_size : (i + 1) * batch_size]
    batch_embeddings = model.encode(batch_lines)
    embeddings.append(batch_embeddings)

if remaining_lines > 0:
    remaining_batch = lines[num_batches * batch_size :]
    remaining_embeddings = model.encode(remaining_batch)
    embeddings.append(remaining_embeddings)

# Concatenate the embeddings into a single numpy array
embeddings = np.concatenate(embeddings, axis=0)

# Compute the cosine similarity between each pair of lines
similarity_matrix = np.dot(embeddings, embeddings.T)

# Find the indices of the two most similar lines
indices = np.unravel_index(similarity_matrix.argmax(), similarity_matrix.shape)

# Print the most similar lines
print(
    f"Line {indices[0] + 1} and Line {indices[1] + 1} are the most similar to each other"
)

# Save the embedding matrix to output.npy
np.save("/usr/local/output/output.npy", embeddings)

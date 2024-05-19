import json
import logging

import numpy as np
from sentence_transformers import SentenceTransformer, util

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config(config_path):
    """Load configuration from a JSON file."""
    logging.info(f"Loading configuration from {config_path}")
    with open(config_path, "r") as file:
        config = json.load(file)
    return config


def load_model(model_name):
    """Load the sentence transformer model."""
    logging.info(f"Loading model: {model_name}")
    return SentenceTransformer(model_name)


def read_input_file(file_path):
    """Read input lines from the specified file."""
    logging.info(f"Reading input file: {file_path}")
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def embed_lines(model, lines, batch_size=2):
    """Embed input lines in batches."""
    logging.info("Embedding lines")
    embeddings = []
    for i in range(0, len(lines), batch_size):
        batch = lines[i : i + batch_size]
        batch_embeddings = model.encode(batch)
        embeddings.extend(batch_embeddings)
    return np.array(embeddings)


def save_embeddings(embedding_matrix, output_path):
    """Save the embedding matrix to a .npy file."""
    logging.info(f"Saving embeddings to: {output_path}")
    np.save(output_path, embedding_matrix)


def find_most_similar_lines(embedding_matrix):
    """Find the two most similar lines based on cosine similarity."""
    logging.info("Computing cosine similarities")
    cosine_similarities = util.pytorch_cos_sim(
        embedding_matrix, embedding_matrix
    ).numpy()
    np.fill_diagonal(cosine_similarities, -np.inf)
    most_similar_pair = np.unravel_index(
        np.argmax(cosine_similarities, axis=None), cosine_similarities.shape
    )
    return most_similar_pair


def main(config_path):
    """Main function to run the process."""
    config = load_config(config_path)
    model = load_model(config["model_name"])
    lines = read_input_file(config["input_file"])
    embedding_matrix = embed_lines(model, lines)
    save_embeddings(embedding_matrix, config["output_file"])
    line_a, line_b = find_most_similar_lines(embedding_matrix)
    logging.info(
        f"Line {line_a + 1} and Line {line_b + 1} are the most similar to each other"
    )


if __name__ == "__main__":
    main("/docker-project/config.json")

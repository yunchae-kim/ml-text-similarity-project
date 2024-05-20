# Text Embedding and Similarity Analysis with Docker

## Project Overview

This simple project involves setting up a Python application within a Docker container
to process text data using a machine learning model. The goal is to embed text
lines using a pre-trained model and find the most similar pairs of lines based
on their embeddings. The project leverages the HuggingFace
`sentence-transformers` library to perform text embeddings.

## Technology Stack

- **Docker**: Containerization of the application.
- **Python 3.11**: The programming language used for the core functionality.
- **HuggingFace**: Specifically, the `sentence-transformers` library to perform text embeddings.
- **NumPy**: For numerical operations and saving the embeddings.

## How to Work on This Project

### Configuration

The project uses a configuration file (`config.json`) to manage paths and model
names. This makes the code modular and easy to update without changing the core
logic.

### Running the Project

1. **Build the Docker Image**:

   ```bash
   docker build -t docker-project .
   ```

2. **Run the Docker Container**:

   ```bash
   ./run.sh
   ```

3. **Export the Docker Container**:
   ```bash
   docker save docker-project -o container.tar
   ```

### Project Structure

- `Dockerfile`: Defines the Docker environment.
- `run.sh`: Script to build and run the Docker container.
- `main.py`: Main script to process the data using the specified model.
- `config.json`: Configuration file to manage model, input, and output paths.
- `requirements.txt`: Python packages requirements for this project.

### Note on Input Data

The script expects the input file to contain exactly 10 lines to work with this
specific sample as an example. If the input file contains a different number of
lines, a warning will be logged. This setup is tailored for the example
provided and may need adjustments for other datasets.

## References

- [AnnaWegmann/Style-Embedding on HuggingFace](https://huggingface.co/AnnaWegmann/Style-Embedding)
- [Sentence-Transformers Documentation](https://www.sbert.net/index.html)

## Code Enhancements

The functions in `main.py` are modularized and logging statements are
incorporated to showcase clean and maintainable code. This demonstrates the
style and structure that could be used in a professional setting.

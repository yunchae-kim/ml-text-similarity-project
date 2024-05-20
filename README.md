# UPenn Application Developer Take-Home Assignment

This README provides an overview of my approach to the assignment.

## Project Approach

To tackle this assignment, I followed a structured approach:

1. Reviewed assignment guidelines and requirements.
2. Set up project structure and initialized Git repository.
3. Created Dockerfile to define Docker container environment.
4. Implemented `run.sh` script to automate building and running Docker container.
5. Developed `main.py` script to perform core functionality using `HuggingFace` model.
6. Resolved challenges, such as `pip` installation error and `find_similar_lines`
   method incorrectly identifying the same lines as most similar.
7. Modularized functions and added logging statements to enhance code quality.
8. Thoroughly tested the implementation.

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

The script expects the input file to contain exactly 10 lines for optimal
performance as per the assignment requirements. If the input file contains a
different number of lines, a warning will be logged.

## Project Duration

Total time spent on the assignment: 2 hours and 30 minutes.

## Code Enhancements

I modularized functions and incorporated logging statements in `main.py` to
showcase my ability to write clean and maintainable code. While this may be
considered an overkill for a small-scale assignment, I wanted to demonstrate
the style and structure I could use if I were to work for this position.

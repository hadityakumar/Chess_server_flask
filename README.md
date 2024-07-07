
## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd Chess_server_flask
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    flask run
    ```

## Usage

1. Start the Flask server.
2. Use the provided endpoints to interact with the chess engines:
    - Random Chess: `/api/random`
    - Stockfish Engine: `/api/stockfish`
    - ML Model: `/api/ml-model`

## Docker

1. Build the Docker image:
    ```sh
    docker build -t chess-engines-backend .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:5000 chess-engines-backend
    ```

## Deployment

This backend is deployed on Microsoft Azure. [server](https://chess-server1.azurewebsites.net/).

## Links

- [Frontend Repository](https://github.com/hadityakumar/Chess_Engines)

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes.

## Contact

For any inquiries, please reach out to [hadityakumar](https://www.linkedin.com/in/hadityakumar/).

---

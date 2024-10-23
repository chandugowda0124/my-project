# Rule Engine with Abstract Syntax Tree (AST)

## Description
This project implements a 3-tier rule engine using Abstract Syntax Tree (AST) to determine user eligibility based on dynamic conditions.

## Features
- Create rules and convert them to AST.
- Combine multiple rules into a single AST.
- Evaluate rules against user data.

## API Endpoints
- `POST /api/create_rule`: Create an AST from a rule string.
- `POST /api/combine_rules`: Combine multiple rules into a single AST.
- `POST /api/evaluate_rule`: Evaluate a rule against user data.

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/your-username/rule-engine-ast.git
    cd rule-engine-ast
    ```

2. Install dependencies:
    ```
    pip install Flask
    ```

3. Initialize the database:
    ```
    python models.py
    ```

4. Run the application:
    ```
    python app.py
    ```

5. Access the API at `http://127.0.0.1:5000/`.

## Testing
Test cases are available for rule creation, combination, and evaluation.

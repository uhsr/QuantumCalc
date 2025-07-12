# QuantumCalc: Numerically-Stable, Arbitrary-Precision Calculator Engine

QuantumCalc provides a robust and highly performant calculator engine designed for numerically-sensitive applications requiring arbitrary precision. Built with a focus on stability and speed, QuantumCalc leverages advanced expression tree parsing and optimized binary arithmetic routines to deliver accurate results across a wide range of platforms. Unlike traditional floating-point calculators that suffer from precision limitations and rounding errors, QuantumCalc allows users to perform calculations with user-defined precision, ensuring accuracy even in complex and iterative computations.

This engine is particularly useful in scientific simulations, financial modeling, and other domains where even minor inaccuracies can lead to significant discrepancies. The core principle behind QuantumCalc is to represent numbers as binary fractions with a variable number of bits, effectively eliminating the inherent limitations of fixed-precision floating-point representations. By utilizing optimized binary arithmetic functions, QuantumCalc achieves performance comparable to floating-point calculations, making it a viable alternative for demanding computational tasks. The modular design allows for easy integration into existing projects and facilitates future expansion with new mathematical functions and operators.

QuantumCalc employs a sophisticated expression parsing system that converts mathematical expressions into abstract syntax trees (ASTs). These ASTs are then traversed and evaluated using custom-built binary arithmetic functions. This approach not only enables support for a wide range of mathematical operations but also allows for efficient optimization of the evaluation process. The engine's modular architecture allows developers to easily extend its functionality by adding new operators, functions, and data types. The result is a flexible and powerful calculation tool that can be tailored to meet the specific needs of various applications.

## Key Features

*   **Arbitrary Precision Arithmetic:** Supports calculations with user-defined precision, eliminating rounding errors associated with fixed-precision floating-point arithmetic. Achieved through custom implementation of binary fractions and optimized arithmetic routines.
*   **Expression Tree Parsing:** Utilizes an advanced expression parsing engine to convert mathematical expressions into abstract syntax trees (ASTs) for efficient evaluation. Supports a wide range of operators, functions, and variables.
*   **Numerically-Stable Algorithms:** Employs numerically-stable algorithms for complex mathematical operations to minimize error propagation and ensure accuracy. Examples include using Kahan summation for accurate summation of large datasets.
*   **Optimized Binary Arithmetic:** Leverages optimized binary arithmetic functions for high-performance calculations, achieving speeds comparable to floating-point calculations. Optimized functions are implemented in C and interfaced with Python using Cython.
*   **Modular Design:** Features a modular architecture for easy integration into existing projects and facilitates future expansion with new mathematical functions and operators. Each module is designed with clear interfaces and documented APIs.
*   **Platform Independent:** Designed to operate seamlessly across multiple platforms, including Windows, macOS, and Linux. Cross-platform compatibility is achieved through standardized C libraries and Python interpreter.
*   **Custom Function Support:** Allows users to define and integrate custom mathematical functions into the calculation engine. The function definition includes input validation and error handling.

## Technology Stack

*   **Python:** The primary programming language used for the calculator engine's core logic and user interface. Python's high-level syntax facilitates rapid development and easy integration.
*   **Cython:** Used to write performance-critical binary arithmetic functions in C and seamlessly integrate them with Python code. This allows for significant performance improvements compared to pure Python implementations.
*   **Abstract Syntax Tree (AST):** Data structure used to represent mathematical expressions in a hierarchical format, enabling efficient evaluation and optimization.
*   **Regular Expressions:** Employed for parsing mathematical expressions and identifying different operators and functions.

## Installation

1.  Clone the repository:
    git clone https://github.com/uhsr/QuantumCalc.git

2.  Navigate to the project directory:
    cd QuantumCalc

3.  Create a virtual environment (recommended):
    python3 -m venv venv
    source venv/bin/activate (Linux/macOS)
    venv\Scripts\activate (Windows)

4.  Install the required dependencies:
    pip install -r requirements.txt

5.  Compile the Cython modules:
    python setup.py build_ext --inplace

## Configuration

QuantumCalc does not rely on external configuration files or environment variables for basic operation. The precision level is controlled directly within the Python code when instantiating the calculator object or performing calculations. For example:

from quantumcalc import Calculator
calc = Calculator(precision=100) # Sets precision to 100 decimal places

This example shows how to set the precision level during object instantiation.

## Usage

Example 1: Basic calculation with specified precision

from quantumcalc import Calculator
calc = Calculator(precision=50)
result = calc.evaluate("3.14159 + 2.71828")
print(result)

Example 2: Using custom functions

from quantumcalc import Calculator
def custom_function(x, y):
    return x * x + y * y
calc = Calculator(precision=20)
calc.register_function("my_func", custom_function, 2) # Function name, function object, number of arguments.
result = calc.evaluate("my_func(2, 3)")
print(result)

API Documentation (Simplified):

*   `Calculator(precision)`: Initializes the calculator with the specified precision.
*   `evaluate(expression)`: Evaluates the given mathematical expression and returns the result.
*   `register_function(name, function, num_args)`: Registers a custom function with the specified name, function object, and number of arguments.

## Contributing

We welcome contributions to QuantumCalc! Please follow these guidelines:

*   Fork the repository and create a branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Adhere to the project's coding style.
*   Include unit tests for any new code.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/QuantumCalc/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their contributions to the libraries and tools used in this project.
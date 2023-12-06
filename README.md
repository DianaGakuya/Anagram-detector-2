# Anagram Detector Lab

This is a Python implementation of an Anagram Detector lab, where a class is built to determine anagrams of a given word from a list.

## Getting Started

Follow the instructions below to set up the project on your local machine.

### Prerequisites

- Python 3.x
- Pipenv (for virtual environment management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deegakuya/Anagram-detector-2


## Navigate to the project directory:
bash
Code
cd anagram-detector


## Create a virtual environment and install dependencies:
bash
Code
pipenv install

## Activate the virtual environment:
bash
Code
pipenv shell
Running Tests

## Make sure to run tests to ensure that the Anagram class is working as expected. Use the following command:
bash
Code
pytest -x

## Usage
Modify the anagram.py file to customize the Anagram class for your specific needs.

## Example usage:

python
Code
from anagram import Anagram
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # Output: ['inlets']


## Contributing
If you'd like to contribute to this project, please follow the standard GitHub flow:

Fork the repository
Create a new branch
Make changes and commit them
Push changes to your fork
Create a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The lab is inspired by the need to practice object-oriented programming and algorithmic thinking.
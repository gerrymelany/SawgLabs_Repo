# Swag Labs Automation Project

**Summary:**
Welcome to the Swag Labs Automation Project! This repository shows a complete set of automated tests for the Swag Labs application (saucedemo.com). Using the power of behavior-driven development (BDD) with the Gherkin syntax and the Behave framework, this project aims to demonstrate best practices in test automation.

**Goals:**

Demonstrate experience: Demonstrate my proficiency in BDD and test automation using Behave and Gherkin.

Comprehensive coverage: Provide a complete set of automated tests covering various user scenarios in the Swag Labs application.

**Key Features:**

Behavior-driven development: Tests are written in Gherkin, a human-readable language that bridges the gap between technical and non-technical stakeholders.

Automated Testing with Behave: Implementation of Gherkin scenarios using Behave, a popular BDD framework for Python.

Real-world scenarios: Automated tests cover critical user flows such as logging in, browsing products, adding items to cart, and completing a purchase.


**Used technology:**

Python: programming language used to write test scripts.

Behave: A BDD Framework for Python.

Selenium WebDriver – For browser automation and interaction with the Swag Labs application.

Gherkin: A language for writing executable specifications that describe behavior.

To begin the project, follow the instructions in the Installation section. You'll find detailed guides on how to set up your environment, run tests, and contribute to the project.


**Technologies and Tools:**

Programming language: Python

BDD Framework: Behave, to define tests based on user behavior.

Testing: Pytest for test execution and device management.

Other tools: Selenium WebDriver for automated UI testing and Git for version control.


## Prerequisites

1. **Python Installation**
   - Download and install Python from [python.org](https://www.python.org/downloads/macos/).
   - Verify the installation:
     ```sh
     $ python3 --version
     ```
     Example output:
     ```
     Python 3.10.11
     ```

2. **ChromeDriver Installation**
   - Download the ChromeDriver compatible with your Chrome browser version from [ChromeDriver downloads](https://chromedriver.chromium.org/downloads).
   - Example version: `ChromeDriver 114.0.5735.90`.

3. **Virtual Environment Setup**
   - Create and activate a virtual environment:
     ```sh
     $ python3 -m venv <nombre_ambiente>
     $ source <nombre_ambiente>/bin/activate
     ```
   - Install required dependencies:
     ```sh
     $ pip install -r requirements.txt
     ```

## Project Setup

1. **Clone the Repository**
   ```sh
   $ git clone https://github.com/yourusername/swag-labs-automation.git
   $ cd swag-labs-automation
   ```

2. **Activate the Virtual Environment**
   ```sh
   $ source <nombre_ambiente>/bin/activate
   ```

3. **Install Dependencies**
   ```sh
   $ pip install -r requirements.txt
   ```

## Running the Tests

1. **Activate the Virtual Environment**
   ```sh
   $ source <nombre_ambiente>/bin/activate
   ```

2. **Run Behave**
   ```sh
   $ behave
   ```

## Tips

1. **Managing Global Packages**
   - Uninstall a globally installed package with dependencies:
     ```sh
     $ pip install pip-autoremove
     $ pip_autoremove selenium -y
     ```

2. **Avoid Storing Scripts in Virtual Environment Directories**
   - Keep your scripts outside the virtual environment directories to ensure they can be executed in different environments.

3. **Synchronizing Dependencies**
   - Save dependencies to a requirements file:
     ```sh
     $ pip freeze > requirements_venv.txt
     ```
   - Add, commit, and push the `requirements_venv.txt` file:
     ```sh
     $ git add requirements_venv.txt
     $ git commit -m "Add requirements file"
     $ git push
     ```
   - Other developers can install dependencies from the file:
     ```sh
     $ pip install -r requirements_venv.txt
     ```

Claro, aquí tienes la sección "Contributing" en inglés, personalizada con la URL de tu proyecto:

---

## Contributing

1. **Fork the repository**:
   - Visit [SwagLabs_Gherkin](https://github.com/gerrymelany/SwagLabs_Gherkin.git) and click the "Fork" button in the upper right corner to create your own copy of the repository.

2. **Clone your forked repository**:
   - Clone your forked repository to your local machine:
     ```sh
     $ git clone https://github.com/your-username/SwagLabs_Gherkin.git
     $ cd SwagLabs_Gherkin
     ```

3. **Create a new branch**:
   - Create a new branch for your feature or fix:
     ```sh
     $ git checkout -b feature/your-feature-name
     ```

4. **Make your changes**:
   - Make changes to your code.

5. **Commit your changes**:
   - Save your changes with a descriptive commit message:
     ```sh
     $ git commit -m 'Add commit description'
     ```

6. **Push to the branch**:
   - Push your changes to GitHub:
     ```sh
     $ git push origin feature/your-feature-name
     ```

7. **Create a new Pull Request**:
   - Go to your forked repository on GitHub and click the "New pull request" button to submit your changes to the original repository.

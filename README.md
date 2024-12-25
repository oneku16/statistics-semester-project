# Project Overview

This project is a web-desktop application built with **Flet** for statistical calculations and data visualization. It allows users to create accounts, perform various statistical calculations, and share their work with others in a collaborative environment. The calculators are modular and extensible, designed to handle common statistical distributions like Normal, Poisson, Binomial, and HyperGeometric.

---

## Technologies Used

- **Flet**: For building the UI as a monolithic web-desktop app.
- **Python 3.11+**: Core programming language.
- **PostgreSQL 17+**: For user management and session handling.
- **Docker**: To containerize the PostgreSQL database for easy deployment.
- **Matplotlib** and **SciPy**: For data visualization and statistical computations.

---

## Installation

### 1. Install Python

Ensure Python 3.11 or later is installed on your system. You can download it from the [official Python website](https://www.python.org/).

### 2. Install PostgreSQL

Install PostgreSQL 17 or later. For detailed instructions, refer to the [PostgreSQL documentation](https://www.postgresql.org/download/).

### 3. Set Up Docker for PostgreSQL

Use the following Docker command to containerize the PostgreSQL database:

```bash
docker run --name stats-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=your_password -p 5432:5432 -d postgres:17
```
### 4. Install Dependencies
Use pip to install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run the App
Start the Flet application:

On local machine run with `shift+F10` (`PyCharm`).
On docker: configure Docker file.

## Calculator Development
The application is designed to load statistical calculators dynamically. To implement a new calculator:

Initialize the Calculator Class
Each calculator should define an `__init__` method, initializing key parameters as properties. These properties must start with param_ to be compatible with the calculator loader class.

Example:
```Python
class MyCustomCalculator:
    def __init__(self, param_a: float, param_b: float):
        self.param_a = param_a
        self.param_b = param_b
```
Define the solve Method
The solve method must return:

A figure (matplotlib object) for visualization.
The calculated area or probability as a numerical value.

Example:
```Python
def solve(self, a=None, b=None):
    # Perform calculations
    area = ...  # Some computation
    fig = ...   # Matplotlib figure
    return area, fig
```

### CalculatorHandler class
The application uses a calculator loader class to dynamically interact with calculators. The loader automatically assigns values to properties starting with param_ and invokes the solve method.

Key Mechanism
The loader inspects all attributes of the calculator class that start with param_ and assigns user inputs to them.
The `__on_solve` method of the loader is responsible for:
Collecting user inputs.
Invoking the calculator's solve method.
Plotting the returned figure and displaying the calculated area.

#### Key Mechanism
- The loader inspects all attributes of the calculator class that start with param_ and assigns user inputs to them.
- The __on_solve method of the loader is responsible for: 
- 1. Collecting user inputs.
- 2. Invoking the calculator's solve method.
- 3. Plotting the returned figure and displaying the calculated area.

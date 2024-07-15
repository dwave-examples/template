**Interested in contributing a code example?** 

Please take a look at our [contribution guidelines](CONTRIBUTING.md) before
getting started. Thank you!

<!-- Before submitting your code, please delete the above code contribution
instructions and this comment as they will not be relevant in your code 
example README.md.-->

# <demo_name>

Describe your example and specify what it is demonstrating. Consider the
following questions:

* Is it pedagogical or a usable application?
* Does it belong to a particular domain such as material simulation or logistics?
* What level of Ocean proficiency does it target (beginner, advanced, professional)?

A clear description allows us to properly categorize your example.

Images are encouraged. If your example produces a visualization, consider
displaying it here.

![D-Wave Logo](static/dwave_logo.svg)

## Installation
You can run this example without installation in cloud-based IDEs that support the [Development Containers specification](https://containers.dev/supporting) (aka "devcontainers").

For development environments that do not support `devcontainers`, install requirements:

```bash
pip install -r requirements.txt
```

If you are cloning the repo to your local system, working in a [virtual environment](https://docs.python.org/3/library/venv.html) is recommended.

## Usage
Your development environment should be configured to [access Leap’s Solvers](https://docs.ocean.dwavesys.com/en/stable/overview/sapi.html). You can see information about supported IDEs and authorizing access to your Leap account [here](https://docs.dwavesys.com/docs/latest/doc_leap_dev_env.html).

### Inputs
If your example requires user input, make sure to specify the input format and any input limitations.
### Outputs
An example program output.

## Demo Types
### User Interface Demo (Dash Framework Template)
The Dash template is intended for demos that would benefit from a user interface. This user interface could include settings to run and customize the problem, an interactive graphical element, and/or tables or charts to compare two different solutions. This template is also useful for demos that are intended for a general audience, as it is more approachable for those without a technical background.

Run the following terminal command to start the Dash app:

```bash
python app.py
```

Access the user interface with your browser at http://127.0.0.1:8050/.

#### Template Files
* [app.py](app.py) contains all the [Dash callback functions](https://dash.plotly.com/basic-callbacks) required to run the Dash app. Any new callbacks should be added to this file.
* [dash_html.py](dash_html.py) contains all the Dash HTML components that generate the UI for the app, including settings like sliders, checkboxes, and text inputs, as well as buttons and tables. If a Dash HTML component needs to be dynamically added to the UI by a Dash callback in `app.py`, it is encouraged to add a function generating this component to `dash_html.py` and call this function from `app.py`.
* [app_configs.py](app_configs.py) contains all configerations and settings for the demo and is intended as a quick way to customize the demo for a specific audience or use case without searching through code. This file is intended for users of the demo and should not be cluttered with settings that are not helpful to the user.
* [z_app.css](z_app.css) contains all custom CSS styling for the demo; any new CSS rules should be added here. Dash reads all files in the `/assets/` directory from top to bottom so `z_app.css` will be the last file to be run and will easily be able to overwrite other styling rules.

#### Template Directories
* `/assets/` is a Dash specific directory and therefore it must not contain subdirectories and its name must not be changed. As previously stated, Dash reads files in this directory from top to bottom, because of this, no imports are necessary. The `base.css` file is a Dash-made file with some basic styling rules; this file should not be edited and its name should not be changed. All CSS files with a `c` prefix are custom CSS files created specifically for this demo template. For maintainability these files should _ideally_ not be altered.
* `/src/` should contain all functional code for the dash demo including solver implementations, Class definitions, etc. This directory is not specific to Dash so subdirectories can be used.

## Problem Description 

Objectives to be optimized: define the goal this example attempts to accomplish by minimizing or maximizing certain aspects of the problem; for example, a production-line optimization might attempt to minimize the time to produce all of the products.

Constraints: aspects of the problem and/or process, with limited or no flexibility, that must be satisfied for solutions to be considered feasible; for example, a production-line optimization might have a limitation that Machine A can only bend 10 parts per hour.

## Model Overview
The clearer your model is presented here, the more useful it will be to others. For a strong example of this section, see [here](https://github.com/dwave-examples/3d-bin-packing#model-overview).

### Parameters
List and define the parameters used in your model.

### Variables
List and define (including type: e.g., "binary" or "integer") the variables solved for in your model.

### Expressions
List and define any combinations of variables used for easier representations of the models.

### Objective
Mathematical formulation of the objective described in the previous section using the listed parameters, variables, etc.

### Constraints
Mathematical formulation of the constraints described in the previous section using the listed parameters, variables, etc.

## Code Overview

A general overview of how the code works in bullet points:

* Here's an example bullet point

## Code Specifics

Notable parts of the code implementation.

This is the place to:

* Highlight a part of the code implementation
* Talk about unusual or potentially difficult parts of the code
* Explain a code decision
* Explain how parameters were tuned

Note: there is no need to repeat everything that is already well-documented in
the code.

## References

A. Person, "Title of Amazing Information", [short link
name](https://example.com/)

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.

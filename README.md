**Interested in contributing a code example?** 

Please take a look at our [contribution guidelines](CONTRIBUTING.md) before
getting started. Thanks!

<!-- Before submitting your code, please delete the above code contribution
instructions and this comment as they will not be relevant in your code 
example README.md.-->

# <demo_name>

Describe your example and specify what it is demonstrating. Consider the
following questions:

* Is it pedagogical or a usable application?
* Does it belong to a particular domain such as material simulation or logistics? 
* What level of Ocean proficiency does it target (beginner, advanced, pro)? 

A clear description allows us to properly categorize your example.

Images are encouraged. If your example produces a visualization, consider
displaying it here.

![D-Wave Logo](dwave_logo.png)

## Usage

A simple command that runs your program. For example,

```bash
python <demo_name>.py
```

### Inputs
If your example requires user input, make sure to specify the input format and any input limitations.
### Outputs
An example program output.

## Problem Description 

Objectives to be optimized: the goals the process attempts to accomplish by minimizing or maximizing certain aspects of the problem to the extent possible; for example, a production-line optimization might attempt to minimize the time to produce all of the products.

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

### Constrains
Mathematical formulation of the constraints described in the previous section using the listed parameters, variables, etc.

## Code Overview

A general overview of how the code works.

We prefer descriptions in bite-sized bullet points:

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

## Adding Equations

If you would like to include math equations to explain parts of your code or repo,
it is recommended to use an external LaTeX renderer, or insert pre-rendered images in the repo.
For example, it's possible to insert a link to the online CodeCogs equation editor which will
render LaTeX in the url; there's also syntax to accommodate darkmode by default in D-Wave's [Leap IDE](https://ide.dwavesys.io).

 - Using a URL LaTeX renderer

`<img style="filter:invert(1)" src="https://latex.codecogs.com/svg.latex?\large\,x_{ik}+x_{jk}-2x_{ik}x_{jk}"> `

The above text in markdown renders the following expression in your markdown readme.

<img style="filter:invert(1)" src="https://latex.codecogs.com/svg.latex?\large\,x_{ik}+x_{jk}-2x_{ik}x_{jk}"> 

Inserting a relative link to the svg in the repository in the `readme_imgs`
folder produces the same result.

 - Inserting a static image

`<img style="filter:invert(1)" src="readme_imgs/expression.svg">`

The above text will render the image currently located at the address in the repository.

<img style="filter:invert(1)" src="readme_imgs/expression.svg">

Note: Please consider that some users may be reading your documentation in darkmode, including Leap users.
This may be difficult for certain static images without the kind of filter above.


## References

A. Person, "Title of Amazing Information", [short link
name](https://example.com/)

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.

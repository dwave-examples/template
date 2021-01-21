# Contribution Guidelines

Thanks for your interest in contributing to dwave-examples! Before getting
started, we encourage you to take a look at this document for some guidelines.

## What We're Looking For

While we have a preference for application oriented examples, we welcome all
examples that demonstrate use of the D-Wave system.

For a list of existing examples, take a look
[here](https://cloud.dwavesys.com/leap/examples/).

## Steps for Contributing

1. Download this repository for a template and implement your example on a
   personal repository. Note: To simplify the code reviewing process, we
   encourage you to use a development branch. This way, the code may be reviewed
   as a pull request.

2. Open an issue on this repository and link to your example. See the following
   section for what to include in your issue.

3. Once your example has been reviewed, ____?

## Issue Template

**Description**

A clear and concise description of the concepts in your project and the problem 
your code solves. Please include any references you used.

**How to run the example**

A short description of how to run your code, including an example.

**Link to your repo**

Include a link to the repository you want to contribute to dwave-examples.

**Environment**
 - Python version: [e.g., 3.9.0]
 - Ocean version: [e.g., 3.0]

**Additional information**

Add any other information.

## Structure

### Files

This template includes all required files.

For users who do not wish to use this template, please make sure that your
example includes the following:

* README.md:
    * We prefer .md over .rst.
    * See this repository's [README](README.md).

* requirements.txt:
    * dwave-ocean-sdk should be unpinned and lower bounded.

* LICENSE:
    * Copy the [LICENSE](LICENSE) file from this repository.

* Tests that are discoverable through `python -m unittest discover`.
    * See the `tests` directory in any of our existing examples for guidance.

Our examples are tested using CircleCI. Feel free to copy the `.circleci/`
directory into your example's root directory. Once approved, we will make sure
that your example is set up on our CircleCI account.

### Code

We use the [pep8](https://www.python.org/dev/peps/pep-0008/) style guide as a baseline.

If your example is lengthy, we encourage modularity for ease of testing.

### Documentation

We use the [Google docstrings convention](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

Take a look at our [How to Contribute](https://docs.ocean.dwavesys.com/en/latest/contributing.html#documentation-and-comments)
guide for more details.

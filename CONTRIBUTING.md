# Contribution Guidelines

Thanks for your interest in contributing to dwave-examples! Before getting
started, we encourage you to take a look at this document for some guidelines.

## Steps for Contributing

1. Implement your example on a personal repository. To simplify the code
   reviewing process, we encourage you to use a development branch. This way,
   the code may be reviewed as a pull request.

2. Open an issue on this repository and link to your example.

3. Once your example has been reviewed, ____?

## Structure

To keep our examples consistent, we encourage you to consider the following:

### Files

All examples should contain:

* README.md: See [README_template.md](README_template.md).

* requirements.txt: dwave-ocean-sdk should be unpinned and lower bounded.

* LICENSE: Copy the [LICENSE](LICENSE) file from this repository.

* Tests that are discoverable through `python -m unittest discover`. See the
  `tests` directory in any of our existing examples for guidance.

Our examples are tested using CircleCI. Feel free to copy the `.circleci/`
directory into your example's root directory. Once approved, we will make sure
that your example is set up on our CircleCI account.

### Code

We use the [pep8](https://www.python.org/dev/peps/pep-0008/) style guide as a baseline.

If your example is lengthy, we encourage modularity for ease of testing.

### Documentation

We use the [Google docstrings convention](https://google.github.io/styleguide/pyguide.html).

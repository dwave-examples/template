# Contribution Guidelines

Thanks for your interest in contributing to dwave-examples! Before getting
started, we encourage you to take a look at this document for some guidelines.

## What We're Looking For

While we have a preference for application oriented examples, we welcome all
examples that demonstrate use of Ocean tools.

For a list of existing examples, take a look
[here](https://cloud.dwavesys.com/leap/examples/).

## Steps for Contributing

1. Clone this repository for a basic template from which to implement your
   example. Alternatively, clone one of our existing examples and modify that
   instead.

2. Open an issue on this repository with a link to your example.

3. D-Wave will fork your repository. We may make a pull request if we would like
   your approval for certain code changes.

## Guidelines

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
    * Examples should comply with the Apache 2.0 License. Please make sure that:
        * All source and test files include a license header (as shown in
            [demo_name.py](demo_name.py))
        * The [LICENSE](LICENSE) file is included in your root directory.

* Tests that are discoverable through `python -m unittest discover`.

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

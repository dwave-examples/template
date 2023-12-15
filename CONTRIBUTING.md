# Contribution Guidelines

Thanks for your interest in contributing to dwave-examples! Before getting
started, we encourage you to take a look at this document for some guidelines.

## What We're Looking For

While we have a preference for application oriented examples, we welcome all
examples that demonstrate use of Ocean tools.

To see our categorized collection of examples, create a free acount on
[Leap](https://cloud.dwavesys.com/leap/signup/) and take a look
[here](https://cloud.dwavesys.com/leap/examples/). You can also find our existing
examples by going through the repositories in
[dwave-examples](https://github.com/dwave-examples).

## Steps for Contributing

1. Follow GitHub's instructions to [create a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
   Alternatively, clone this repository (or one of our existing examples) as a 
   starting point from which to implement your example.

2. [Open an issue on the dwave-examples/template repository](https://github.com/dwave-examples/template/issues/new/choose)
   with a link to your example.

3. To add your example, D-Wave will fork your repository. We may make a pull
   request if we would like your approval for certain code changes.

## Guidelines

### Files

Please make sure that your example includes the following:

* `README.md`:
    * We prefer `.md` over `.rst`.
    * See this repository's [README](README.md).

* `requirements.txt`:
    * `dwave-ocean-sdk` should be unpinned and lower bounded.

* `LICENSE`:
    * Examples should comply with the Apache 2.0 License. Please make sure that:
        * All source and test files include a license header (as shown in
            [`demo_name.py`](demo_name.py))
        * The [`LICENSE`](LICENSE) file is included in your root directory.

* Tests that are discoverable through `python -m unittest discover`.

Our examples are tested using CircleCI. For a list of operating systems and
Python versions we currently test our examples with, please take a look at our
documentation
[here](https://docs.ocean.dwavesys.com/en/stable/overview/install.html).

Feel free to copy the [`.circleci/`](.circleci/) directory into your example's root directory.
Once approved, we will make sure that your example is set up on our CircleCI
account.

To ensure your example runs in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview),
copy the [`.devcontainer/`](.devcontainer/) directory into your example's root directory.

### Code

We use the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide as a baseline.

If your example is lengthy, we encourage modularity for ease of testing.

### Documentation

We use the [Google docstrings convention](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

Take a look at our [How to Contribute](https://docs.ocean.dwavesys.com/en/latest/contributing.html#documentation-and-comments)
guide for more details.

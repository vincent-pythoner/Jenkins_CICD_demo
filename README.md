# Jenkins CI/CD Demo

This is a simple calculator package to demonstrate a Jenkins CI/CD pipeline.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -e .



It is local cloned file path.
workflow:
1. make change and git push to github.
2. CICD server knows the git source, will trigger the change (poll scm).
3. CICD server clone the code in pipeline stage 'Checkout'.
4. CICD run python test cases in stage 'Test'. 

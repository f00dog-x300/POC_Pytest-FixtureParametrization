# Proof of Concept of using functions as arguments for parameters

Shows proof of concept for creation utilizing functions as arguments in tests in order to pass information from other sources such as excel files. 

## What are we trying to solve? 

When doing parameterization, we're usually limited to what we pass on our pytest fixtures. However, we can potentially extend that via: 

- indirect parameterization
- using functions to act as readers for the test data

## Where did we implement it? 

See `test_indirect_list.py` 
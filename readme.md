# Project Install Instructions

## Install

1. Clone
2. pip install -r requirements.txt

## We will be Testing folloeing things in this project

1. pytest
2. pytest --pylint
3. pytest --pulint --cov 

The Calulator code consist of basic implementation of a calculator using Command and Plugins. 

The Main file divert to calculator's initialization file which has all the functionality
It also has test files as the branches.

The command folder includes abstract class and an abstract method which is inherited in the individual commands.

## This Repo has 2 branches:

### 1. Command (Merged into the Main Branch)

This branch will implement the code using Command Pattern. I refered previous assigment for this and incorporated operations as commands with each command having initialization file (__init__.py). The command folder includes abstract class and an abstract method which is inherited in the individual commands.

### 2. Plugins (Separate Branch)
To avoid repeatition (voilation of SOLID programming) we include plugins where all the plugins are separated and a loop it added to the command initalization file to call it and run it's functionality.



#! /usr/bin/env python3

from main import fizzBuzz

assert fizzBuzz(1) == "1"
assert fizzBuzz(3) == "Fizz"
assert fizzBuzz(15) == "FizzBuzz"
assert fizzBuzz(60) == "FizzBuzz"
assert fizzBuzz(99) == "Fizz"
assert fizzBuzz(100) == "Buzz"
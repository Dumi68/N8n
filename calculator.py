"""
calculator.py

Simple, readable calculator for junior developers.

Features:
- Basic operations implemented as small functions with type hints
- CLI using argparse (positional operation and two numbers)
- Interactive mode when no arguments are provided
- Friendly error messages for invalid input (e.g., division by zero)

Usage examples:
  python calculator.py add 4 5
  python calculator.py div 10 0
  python calculator.py           # interactive mode

This file is intentionally simple and documented for readability.
"""

from __future__ import annotations
import argparse
from typing import Tuple


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def modulus(a: float, b: float) -> float:
    """Return a modulo b.

    Uses Python's % operator. Raises ValueError when b == 0.
    """
    if b == 0:
        raise ValueError("Modulus by zero is not allowed")
    return a % b


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments and return the namespace."""
    parser = argparse.ArgumentParser(
        description="Simple calculator: add, sub, mul, div, pow, mod"
    )
    parser.add_argument(
        "operation",
        nargs="?",
        choices=["add", "sub", "mul", "div", "pow", "mod", "all"],
        help="Operation to perform",
    )
    parser.add_argument("a", nargs="?", type=float, help="First number")
    parser.add_argument("b", nargs="?", type=float, help="Second number")
    return parser.parse_args()


def interactive_prompt() -> Tuple[float, float, str]:
    """Prompt the user for an operation and two numbers.

    Returns a tuple: (a, b, operation)
    """
    print("Interactive mode. Enter 'q' at any prompt to quit.")
    while True:
        op = input("Operation [add, sub, mul, div, pow, mod, all]: ").strip()
        if not op:
            print("Please enter an operation.")
            continue
        if op == "q":
            raise SystemExit(0)
        if op not in ("add", "sub", "mul", "div", "pow", "mod", "all"):
            print("Unknown operation. Try again.")
            continue
        break

    def read_number(prompt: str) -> float:
        while True:
            raw = input(prompt).strip()
            if raw == "q":
                raise SystemExit(0)
            try:
                return float(raw)
            except ValueError:
                print("Not a valid number. Try again or enter 'q' to quit.")

    a = read_number("First number: ")
    b = read_number("Second number: ")
    return a, b, op


def main() -> None:
    """Main entry point: parse args or enter interactive prompt and run the operation."""
    args = parse_args()

    if args.operation is None:
        # Enter interactive mode
        try:
            a, b, op = interactive_prompt()
        except SystemExit:
            print("Goodbye!")
            return
    else:
        if args.a is None or args.b is None:
            print("Both numbers (a and b) must be provided when using the command line.")
            print("Example: python calculator.py add 4 5")
            return
        a, b, op = args.a, args.b, args.operation

    # Map operation names to functions
    ops = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
        "pow": power,
        "mod": modulus,
    }

    try:
        if op == "all":
            print(f"add: {a} + {b} = {add(a,b)}")
            print(f"sub: {a} - {b} = {subtract(a,b)}")
            print(f"mul: {a} * {b} = {multiply(a,b)}")
            try:
                print(f"div: {a} / {b} = {divide(a,b)}")
            except ValueError as e:
                print(f"div: Error: {e}")
            print(f"pow: {a} ^ {b} = {power(a,b)}")
            try:
                print(f"mod: {a} % {b} = {modulus(a,b)}")
            except ValueError as e:
                print(f"mod: Error: {e}")
        else:
            func = ops[op]
            result = func(a, b)
            print(f"Result: {a} {op} {b} = {result}")
    except ValueError as e:
        # Friendly error for things like division/modulus by zero
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

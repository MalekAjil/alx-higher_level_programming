#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except Exception:
        return (None)
    finally:
        return (c)

import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract,multiply,divide

#Faker is used to generate random data for testing
fake=Faker()


def generate_test_data(num_records):
    operation_map = {
        'add':add,
        'subtract':subtract,
        'multiply': multiply,
        'divide':divide
    }

    for i in range (num_records):
        a=Decimal(fake.random_number(digits=2))
        b=Decimal(fake.random_number(digits=2)) if i%4!=3 else Decimal(fake.random_number(digits=1))
        operation_name=fake.random_element(elements=list(operation_map.keys()))
        operation_func = operation_map[operation_name]

        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
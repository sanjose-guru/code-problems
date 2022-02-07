import sol

nf = sol.NthFibonacci()


def test_fib():
    assert nf.fib(6) == 8
    assert nf.fib(7) == 13
    assert nf.fib(8) == 21
    assert nf.fib(50) == 12586269025

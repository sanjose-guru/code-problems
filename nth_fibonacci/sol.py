class NthFibonacci:
    def fib(self, n: int) -> int:
        nthFib = [0] * (n+1)
        nthFib[1] = 1
        for i in range(n):
            if i+1 <= n:
                nthFib[i+1] += nthFib[i]
            if i+2 <= n:
                nthFib[i+2] += nthFib[i]

        return nthFib[n]


nf = NthFibonacci()
print(f"{nf.fib(6)}")

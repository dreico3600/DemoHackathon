import sys

def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Debe proporcionar un número entero n como argumento.")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("El argumento debe ser un número entero.")
        sys.exit(1)
    result = generate_fibonacci(n)
    print(",".join(str(num) for num in result))

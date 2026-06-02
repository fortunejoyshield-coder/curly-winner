import math

def factormerssine(p, k):
    # returns 0 if (2pk+1) divides 2^p - 1
    return gmpy2.powmod(2,p, 2*p*k+1)-1

import time

import time

def save_progress(p, k, q):
    with open("progress.txt", "w") as f:
        f.write(f"{p},{k},{q}\n")
import gmpy2
def factorfromctod(c, d, p):

    twop = p << 1

    k = (c + twop - 1) // twop
    q = twop * k + 1

    start = time.time()
    last_k = k

    while q < d:

        if ((q & 7) in (1, 7)
            and q % 3
            and q % 5
            and q % 7
            and q % 11):

            if factormerssine(p, k) == 0:
                print(f"\nFOUND FACTOR: q = {q}")
                save_progress(p, k, q)
                report("F")
                return q

        if k % 100000 == 0:
            elapsed = time.time() - start
            scanned = k - last_k
            rate = scanned / elapsed if elapsed > 0 else 0

            remaining_q = (d - q) // twop
            eta_seconds = remaining_q / rate if rate > 0 else float('inf')

            pct = 100 * (q - c) / (d - c)

            print(
                f"\r{pct:.3f}% | ETA: {eta_seconds/3600:.2f}h "
                f"({eta_seconds/60:.1f}m)",
                end="",
                flush=True
            )

            save_progress(p, k, q)

            start = time.time()
            last_k = k

        k += 1
        q += twop

    print()
    save_progress(p, k, q)
    report("NF")
    return None

def report(result):
    print("Result:", result)


def read_line_fast(filename, c):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines[c-1].rstrip("\n")



def floor_pow2_rational(a, b):
    lo, hi = 0, 1 << ((a + b - 1) // b + 1)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** b <= (1 << a):
            lo = mid
        else:
            hi = mid

    return lo

def getassigment():
    c = 1

    while True:
        line = read_line_fast("assigments.txt", c)

        parts = line.split("=")[1].split(",")

        if parts[-1].strip() == "U":
            return [parts[1], parts[2]]

        c += 1
        with open("c.txt", "w") as f:
            f.write(f"c\n")












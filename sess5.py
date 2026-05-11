import numpy as np


def main():
    # Create 1000 x-values between 0 and 2
    x = np.linspace(0, 2, 1000)

    # Compute sin(x)
    y = np.sin(x)

    # Print table header
    print(f"{'x':>12} {'sin(x)':>12}")

    # Print table values
    for xi, yi in zip(x, y):
        print(f"{xi:12.6f} {yi:12.6f}")


if __name__ == "__main__":
    main()

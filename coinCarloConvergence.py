import random
import matplotlib.pyplot as plt


def main():
    trials = 1_000_000
    step = 1000
    y = []
    outcome = 0
    favorable = 0
    for trial in range(1, trials + 1):
        if outcome == 1:
            favorable += 1
        if trial % step == 0:
            y.append(favorable / trial)
        outcome = random.randint(0, 1)

    x = range(step, trials + 1, step)

    plt.figure(figsize=(10, 6))

    plt.plot(x, y)

    plt.axhline(0.5, color="red", linestyle="--", label="True Value (0.5)")

    plt.xlabel("Number of Trials Ran")
    plt.ylabel("Estimated Probability")
    plt.title("Monte Carlo Convergence Test of a Coin Flip")

    plt.legend()
    plt.grid(True)
    plt.show()

    calculatedProbability = favorable / trials * 100
    print(f"Final Estimated Probability: {calculatedProbability}%")


if __name__ == "__main__":
    main()

from Presenter import Presenter


def main():
    K = 2
    M = 5
    N = 5

    solver = Presenter(K, M, N)
    solver.run_algorithm()


if __name__ == "__main__":
    main()


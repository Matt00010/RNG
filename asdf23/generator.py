def generate_randome_number():
    return 23  # chosen by fair dice roll.


def main():
    print(f"Your random number is: {generate_randome_number()}")


if __name__ == "__main__":
    import dis

    dis.dis(generate_randome_number)
    main()

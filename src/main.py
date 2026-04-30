from datetime import date

from utils import add, subtract

def main():
    try:
        print('Debotos')
        print(date.today())

        result_add = add(5, 3)
        result_sub = subtract(5, 3)

        print(result_add)
        print(result_sub)

    except TypeError as e:
        print(f"Type error occurred: {e}")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
from hibp import HIBP


def main():
    hibp = HIBP()
    print("\n\nBREACHED ACCOUNT")
    print(
        hibp.breached_account(
            "olivier.loustaunau@gmail.com", unverified=True, truncate=False
        )
    )
    print("\n\nBREACHES")
    print(hibp.breaches(domain="adobe.com"))
    print("\n\nBREACH")
    print(hibp.breach("Canva"))
    print("\n\nDATA CLASSES")
    print(hibp.data_classes())
    print("\n\nPASTE ACCOUNT")
    print(hibp.paste_account("olivier.loustaunau@gmail.com"))


if __name__ == "__main__":
    main()

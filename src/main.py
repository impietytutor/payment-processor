from payment_processor.config import Config
from payment_processor.db import Database
from payment_processor.services import PaymentService

def main():
    config = Config()
    db = Database(config.db_url)
    payment_service = PaymentService(db)

    while True:
        print("1. Process Payment")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            payment_id = input("Enter payment ID: ")
            payment_service.process_payment(payment_id)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
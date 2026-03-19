"""
payment-processor: A Python package for processing payments.

This package provides a simple and efficient way to process payments
using various payment gateways.

Installation
------------

To install the payment-processor package, run the following command:

    pip install payment-processor

Usage
-----

To use the payment-processor package, import it and create an instance
of the PaymentProcessor class:

    from payment_processor import PaymentProcessor

    processor = PaymentProcessor('your_payment_gateway_token')

    processor.charge_card('1234-5678-9012-3456', 100)

API Documentation
-----------------

For a full list of available methods and their documentation, please see
the API documentation.

"""

class PaymentProcessor:
    def __init__(self, token):
        self.token = token

    def charge_card(self, card_number, amount):
        # Simulate a charge to a card
        return {
            'status': 'success',
            'message': 'Charge successful',
            'transaction_id': '1234567890'
        }

    def refund_transaction(self, transaction_id):
        # Simulate a refund of a transaction
        return {
            'status': 'success',
            'message': 'Refund successful'
        }

    def get_transaction_history(self):
        # Simulate a list of transactions
        return [
            {'id': '1234567890', 'amount': 100, 'status': 'success'},
            {'id': '9876543210', 'amount': 200, 'status': 'failed'}
        ]

def main():
    processor = PaymentProcessor('your_payment_gateway_token')
    processor.charge_card('1234-5678-9012-3456', 100)
    print(processor.get_transaction_history())

if __name__ == '__main__':
    main()
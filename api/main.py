import os
import json
import logging
from typing import Dict, Optional
from dataclasses import dataclass
import stripe

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class PaymentConfig:
    api_key: str
    currency: str = 'usd'

class PaymentProcessor:
    def __init__(self, config: PaymentConfig):
        self.config = config
        stripe.api_key = config.api_key

    def create_payment_intent(
        self,
        amount: int,
        description: str,
        metadata: Optional[Dict[str, str]] = None
    ) -> stripe.PaymentIntent:
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=self.config.currency,
                description=description,
                metadata=metadata or {}
            )
            logger.info(f"Created payment intent: {intent.id}")
            return intent
        except stripe.error.StripeError as e:
            logger.error(f"Failed to create payment intent: {str(e)}")
            raise

    def confirm_payment(self, payment_intent_id: str) -> stripe.PaymentIntent:
        try:
            intent = stripe.PaymentIntent.confirm(payment_intent_id)
            logger.info(f"Confirmed payment intent: {intent.id}")
            return intent
        except stripe.error.StripeError as e:
            logger.error(f"Failed to confirm payment intent: {str(e)}")
            raise

def load_config() -> PaymentConfig:
    config_path = os.getenv('PAYMENT_CONFIG_PATH', 'config.json')
    try:
        with open(config_path) as f:
            config_data = json.load(f)
        return PaymentConfig(**config_data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load config: {str(e)}")
        raise

def main():
    try:
        config = load_config()
        processor = PaymentProcessor(config)
        
        # Example usage
        intent = processor.create_payment_intent(
            amount=1000,
            description="Test payment",
            metadata={"order_id": "12345"}
        )
        print(f"Payment intent created: {intent.id}")
    except Exception as e:
        logger.error(f"Payment processing failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
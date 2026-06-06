"""
BankingBotEnglish — AWS Lambda Function
========================================
Handles fulfillment for the BankerBot Amazon Lex V2 chatbot.
Processes CheckBalance and TransferFunds intents.

Author: Your Name
Project: NextWork AWS Amazon Lex Chatbot Series
"""

import json
import random
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# ---------------------------------------------------------------------------
# Helper: Build Lex response objects
# ---------------------------------------------------------------------------

def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']


def get_slot(intent_request, slot_name):
    slots = get_slots(intent_request)
    if slots is None or slot_name not in slots or slots[slot_name] is None:
        return None
    return slots[slot_name]['value']['interpretedValue']


def get_session_attributes(intent_request):
    session_state = intent_request['sessionState']
    return session_state.get('sessionAttributes', {})


def elicit_slot(intent_request, session_attributes, slot_to_elicit, message):
    """Ask the user to provide a specific slot value."""
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'ElicitSlot',
                'slotToElicit': slot_to_elicit
            },
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        'requestAttributes': intent_request.get('requestAttributes', {})
    }


def confirm_intent(intent_request, session_attributes, message):
    """Ask the user to confirm the intent before fulfillment."""
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {'type': 'ConfirmIntent'},
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        'requestAttributes': intent_request.get('requestAttributes', {})
    }


def close(intent_request, session_attributes, fulfillment_state, message):
    """Close the intent with a final response."""
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {'type': 'Close'},
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        'requestAttributes': intent_request.get('requestAttributes', {})
    }


def delegate(intent_request, session_attributes):
    """Hand control back to Lex to continue dialog management."""
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {'type': 'Delegate'},
            'intent': intent_request['sessionState']['intent']
        },
        'requestAttributes': intent_request.get('requestAttributes', {})
    }


# ---------------------------------------------------------------------------
# Mock data helpers
# ---------------------------------------------------------------------------

def get_mock_balance(account_type):
    """Return a mock account balance. Replace with real DB lookup."""
    balances = {
        'checking': round(random.uniform(500, 5000), 2),
        'savings':  round(random.uniform(1000, 20000), 2),
        'credit':   round(random.uniform(0, 3000), 2),
    }
    return balances.get(account_type.lower(), 0.00)


def validate_date_of_birth(dob_str):
    """Validate that the date of birth is a real past date."""
    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d')
        if dob >= datetime.now():
            return False, "Date of birth must be in the past."
        if dob.year < 1900:
            return False, "That date seems too far in the past. Please try again."
        return True, None
    except ValueError:
        return False, "I didn't catch that date. Please use YYYY-MM-DD format."


# ---------------------------------------------------------------------------
# Intent handlers
# ---------------------------------------------------------------------------

def check_balance(intent_request):
    """Handle the CheckBalance intent."""
    session_attributes = get_session_attributes(intent_request)
    source = intent_request.get('invocationSource', 'FulfillmentCodeHook')

    account_type = get_slot(intent_request, 'accountType')
    date_of_birth = get_slot(intent_request, 'dateOfBirth')

    logger.info(f"CheckBalance — accountType={account_type}, dob={date_of_birth}")

    # ---- Slot validation (DialogCodeHook) ----
    if source == 'DialogCodeHook':
        if date_of_birth:
            valid, error_msg = validate_date_of_birth(date_of_birth)
            if not valid:
                return elicit_slot(
                    intent_request,
                    session_attributes,
                    'dateOfBirth',
                    {
                        'contentType': 'PlainText',
                        'content': error_msg
                    }
                )
        return delegate(intent_request, session_attributes)

    # ---- Fulfillment ----
    balance = get_mock_balance(account_type)
    response_text = (
        f"Thank you for verifying your identity! "
        f"Your {account_type} account balance is ${balance:,.2f}. "
        f"Is there anything else I can help you with?"
    )

    return close(
        intent_request,
        session_attributes,
        'Fulfilled',
        {'contentType': 'PlainText', 'content': response_text}
    )


def transfer_funds(intent_request):
    """Handle the TransferFunds intent."""
    session_attributes = get_session_attributes(intent_request)
    source = intent_request.get('invocationSource', 'FulfillmentCodeHook')

    source_account  = get_slot(intent_request, 'sourceAccount')
    target_account  = get_slot(intent_request, 'targetAccount')
    transfer_amount = get_slot(intent_request, 'transferAmount')

    logger.info(
        f"TransferFunds — from={source_account}, to={target_account}, "
        f"amount={transfer_amount}"
    )

    if source == 'DialogCodeHook':
        # Validate that source and target accounts are different
        if source_account and target_account:
            if source_account.lower() == target_account.lower():
                return elicit_slot(
                    intent_request,
                    session_attributes,
                    'targetAccount',
                    {
                        'contentType': 'PlainText',
                        'content': (
                            "The source and target accounts must be different. "
                            "Which account would you like to transfer funds TO?"
                        )
                    }
                )
        return delegate(intent_request, session_attributes)

    # Fulfillment
    response_text = (
        f"Done! I've transferred ${float(transfer_amount):,.2f} "
        f"from your {source_account} account to your {target_account} account. "
        f"Is there anything else I can help you with?"
    )

    return close(
        intent_request,
        session_attributes,
        'Fulfilled',
        {'contentType': 'PlainText', 'content': response_text}
    )


def welcome(intent_request):
    """Handle the WelcomeIntent."""
    session_attributes = get_session_attributes(intent_request)
    return close(
        intent_request,
        session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': (
                "Hello! Welcome to BankerBot, your AI-powered banking assistant. "
                "I can help you check your account balance or transfer funds between accounts. "
                "What would you like to do today?"
            )
        }
    )


def fallback(intent_request):
    """Handle the FallbackIntent."""
    session_attributes = get_session_attributes(intent_request)
    return close(
        intent_request,
        session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': (
                "I'm sorry, I didn't quite understand that. "
                "I can help you check your account balance or transfer funds. "
                "Which would you like to do?"
            )
        }
    )


# ---------------------------------------------------------------------------
# Main Lambda handler
# ---------------------------------------------------------------------------

INTENT_HANDLERS = {
    'WelcomeIntent':   welcome,
    'CheckBalance':    check_balance,
    'TransferFunds':   transfer_funds,
    'FallbackIntent':  fallback,
}


def lambda_handler(event, context):
    """
    Entry point for the Lambda function.
    Routes requests to the appropriate intent handler.
    """
    logger.info(f"Event: {json.dumps(event)}")

    intent_name = event['sessionState']['intent']['name']
    logger.info(f"Dispatching intent: {intent_name}")

    handler = INTENT_HANDLERS.get(intent_name)
    if handler:
        return handler(event)

    raise Exception(f"Intent '{intent_name}' not supported by this Lambda function.")

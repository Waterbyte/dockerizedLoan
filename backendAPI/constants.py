from enum import  Enum

class misc_webargs(Enum):
    USERNAME = 1
    PASSWORD = 2
    TOKEN = 3
    ROLE = 4
    REFERRER_USERNAME = 5
    REFERRER_TOKEN = 6
    TIMESTAMP=7
    AGENT_NAME = 8
    CUSTOMER_NAME = 9

class response(Enum):
    VERDICT = 101
    PAYLOAD = 102

class collectionName(Enum):
    users = 201
    relations = 202
    loan_inventory = 203

class roles(Enum):
    ADMIN = 301
    AGENT = 302
    CUSTOMER = 303

class loan(Enum):
    ID = 401
    NAME = 402
    DESC = 403
    MINLIMIT = 404
    MAXLIMIT = 405
    MIN_DURATION = 406
    MAX_DURATION = 407
    INTERESTRATE = 408
    MANDATORY_REQUIREMENT1 = 409
    MANDATORY_REQUIREMENT2 = 410
    EMI_AVAILABLE = 411
    PREPAYMENT_AVAILABLE = 412
    PREPAYMENT_CHARGES = 413
    LOAN_PROCESSING_CHARGES = 414
    EXTRA_ONE_TIME_CHARGES = 415
    MINIMUM_CREDIT_SCORE = 416
    MINIMUM_ANNUAL_INCOME_LOANEE = 417
    MINIMUM_MONTHLY_INCOME_LOANEE = 418

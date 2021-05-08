import hashlib


class NambiCoin():


    # Our Special Constructor Method of our class:

    def __init__(self, previous_block_hash, latest_transaction_list):


        self.previous_block_hash = previous_block_hash


        self.latest_transaction_list = latest_transaction_list

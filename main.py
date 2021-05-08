import hashlib


class NambiCoinBlock():


    # Our Special Constructor Method of our class:

    def __init__(self, previous_block_hash, latest_transaction_list):


        self.previous_block_hash = previous_block_hash


        self.latest_transaction_list = latest_transaction_list


        self.block_data = "-".join(latest_transaction_list) + "-" + previous_block_hash


        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



        # hexdigest() method returns the hexadecimal code in the form of a string object.



# Now, let's perform some transactions.


t1 = "Aditya sends 2.0 NBC to Ramesh."

t2 = "Ramesh sends 4.1 NBC to Ahilya."

t3 = "Gaurav sends 3.2 NBC to Aditya."

t4 = "Aditya sends 4.22 NBC to Ahilya."

t5 = "Ramesh sends 7.1234 NBC to Gaurav."

t6 = "Mathew sends 9.260 NBC to Aditya."

t7 = "Ravish sends 2.1245 NBC to Ramesh."



genesis_block = NambiCoinBlock("Genesis Block", [t1, t2])


# genesis_block is the "initial" Nambi Coin block.

# genesis_block is an "instance" of the NambiCoinBlock class.


print()


print(genesis_block.block_data)


print()


# print(type(genesis_block.block_hash))


print(genesis_block.block_hash)

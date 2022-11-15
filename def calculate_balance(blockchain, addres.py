from backend.config import STARTING_BALANCE


def calculate_balance(blockchain, address):
        """
        Calculate the balance of the given address considering the transaction of data
        within the blockchain.

        The balance is found by adding the output values that belong to the address
        since the most recent transaction by that address.
        """
        STARTING_BALANCE = 1000
        
        balance = STARTING_BALANCE

        for block in blockchain.chain:
            for transaction in block.data:
                if transaction['input']['address'] == address:
                    #Any time the address conducts a new transaction it resets
                    #its balance.
                    balance = transaction['output'][address]
                elif address in transaction['output']:
                    balance += transaction['output'][address]
            
        return balance
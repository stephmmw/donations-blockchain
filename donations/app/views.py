from django.shortcuts import render
from datetime import datetime
import time
import hashlib

# Create your views here.

class BlockChain():
    blocks = []
    __difficulty = 1
    secret = '' # Generated during each record insertion Used to make each hash unique
    key = 'D0n@t!0n$Am@UnT' # Used for hashing
    
    def __init__(self):
        nonce = 0 # Guess the nonce
        
        while True:
            donation_hash = hashlib.sha512(str(self.key + str(nonce)).encode('utf-8')).hexdigest()
            if donation_hash[:self.__difficulty] == '0' * self.__difficulty:
                self.secret = donation_hash
                break
            nonce += 1
    
    # Create A block in the chain        
    def add_block(self, data:dict):
        block = {
            "index": len(self.blocks),
            "data": data,
            "timestamp": datetime.now(),            
        }
        if block['index'] == 0: 
            block['last_hash'] = self.secret # For Origin block
            
        else: 
            block['last_hash'] = self.blocks[-1]['hash']
        
        # guess the nonce
        nonce = 0
        while True:
            block['nonce'] = nonce
            donation_hash = hashlib.sha256(str(block).encode('utf-8')).hexdigest()
            if donation_hash[:self.__difficulty] == '0' * self.__difficulty:
                block['hash'] = donation_hash
                break
            nonce+=1
            
        self.blocks.append(block)

    # Check chain validity
    def validate(self):
        valid = True
        n = len(self.blocks)-1 # Length of the chain
        i = 0
        while(i<n):
            if(self.blocks[i]['hash'] != self.blocks[i+1]['last_hash']):
                valid = False
                break
            i+=1
        if valid:
            print('\nStatus:'+'Ok'+ '\nMessage:'+ 'Valid block Chain')
        else: 
            print('\nStatus:'+'Bad'+ '\nMessage:'+ 'Invalid block Chain')
    
    # Display Chain
    def display(self):
        print("\n")
        for block in self.blocks :
            print(block,"\n")
    
# Interface
def index(request):
    chain = BlockChain()
    
    if request.method == "POST":
        timestamp = str(datetime.now())
        name = request.POST["name"]
        amount = request.POST["amount"] 
        
        data = {"name": name, "amount": amount, "donation_time": timestamp}
        chain.add_block(data)
        chain.validate()
        chain.display()
    
    app = 'Donations'
    context = {
        "app": app,
        "title": 'Donations',
    }
    template_name = "index.html"
    return render(request, template_name, context)
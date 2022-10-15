import hashlib
def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()
class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash
class Blockchain:
    def __init__(self):
        hashLast=hashGenerator('gen_last')
        hashStart=hashGenerator('gen_hash')

        genesis=Block('gen_data',hashStart,hashLast)
        self.chain=[genesis]
    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)
bc=Blockchain()
getcode=input("Enter your input to create hash:")
bc.add_block(getcode)
getcode=input("Enter your next input to create hash:")
bc.add_block(getcode)
getcode=input("Enter your next input to create hash:")
bc.add_block(getcode)
for block in bc.chain:
    print(block.__dict__)
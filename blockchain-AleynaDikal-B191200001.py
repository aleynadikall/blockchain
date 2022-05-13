import hashlib
from time import time
import random
import json
from pprint import pprint


#Blockchain Classı
class Blockchain(object):
    def __init__(self):
        self.blockChainArray=[]
        self.nonceArray=[]
        print("run:",end="\n")
        self.newNode("0000000000000000000000000000000000000000000000000000000000000000")
        
    #Düğüm ekleyen methot
    def newNode(self,previousHash=''):
        arrayElement={
            'id':len(self.blockChainArray),
            'nonce':self.generateNonce(),
            'timeStamp':time(),
            'hash':hashlib.sha256(previousHash.encode()).hexdigest(),
            'previousHash':previousHash or self.blockChainArray[-1]['hash'],
            'transaction':'transaction'+ str(len(self.blockChainArray)+1)
        }
        #Blockchain zincirlerini tutan arraye elemanın eklenmesi
        self.blockChainArray.append(arrayElement)
        #Ekrana istenilen formatta yazdırma işlemi
        print(arrayElement['id'],arrayElement['transaction'],arrayElement['hash'],arrayElement['previousHash'],'has just minted...',sep='-',end='\n')
        print("Hash is:",arrayElement['hash'],end='\n')
        
    """
    Nonce elemanı oluşturma işlemi her bir nonce birbirinden eşsiz olması gerektiği için 
    önceden bulunan elemanlar kontrol edilmiş ve o şekilde atama işlemi yapılmıştır.
    
    """
    def generateNonce(self):
         possibleNonce=random.randint(0,1000)
         if(possibleNonce in self.nonceArray):
             possibleNonce=random.randint(0,1000)
         else:
             self.nonceArray.append(possibleNonce)
             return possibleNonce
        
    """
    Blockchain array elemanlarını ekrana bastıran method
    """
    def printBlockChain(self):
        print('',end='\n')
        print("BLOCKCHAIN:",end='\n')
        for i in self.blockChainArray:
            print(i['id'],i['transaction'],i['hash'],i['previousHash'],sep='-')
            
    """
    Ekrana blockchain arrayin daha düzgün gözükücek şekilde bastırılmasını sağlayan methot
    """            
    def printBlockChainPrettify(self):
        print('',end='\n')
        print('The block chain:',end='\n')
        pprint(self.blockChainArray)
        
        
    """
    Ödülü hesaplayan fonksiyon
    """
    def calculateReward(self):
        print("",end="\n")
        print("Reward:",len(self.blockChainArray)*100)
    
    

        

blockchain = Blockchain()

node1 = blockchain.newNode()
node2 = blockchain.newNode()

blockchain.printBlockChain()
blockchain.printBlockChainPrettify()
blockchain.calculateReward()

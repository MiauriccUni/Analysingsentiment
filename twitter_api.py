import json


# def tweets(myJson):
    
#     with open(myJson) as content:
   
#         data = json.load(content)
     
#         print(data[1])
        
def tweets(myJson):
    with open(myJson) as content:
        data = json.load(content)
        
        #instanc
        item = data[1]
        
        print(item)
        
        print(f'Type of item: {type(item)}')

    


if __name__=='__main__':
    
    myJson = 'tweets_extraction (1).json'
    
    tweets(myJson)


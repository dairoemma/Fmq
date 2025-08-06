store = {}#store data

# set 
def handle_set(*args):
    try:
        # need just key and value
        if len(args) != 2:
            return {"Error": "SET needs 2 args"}
        
        key = args[0]
        value = args[1]
        store[key] = value
        return {"SUCCESS": "Stored data succesfully"}
    
    except Exception as e:
        return {"Error":f"SET failed: {str(e)}"}

# multiple set 
def handle_mset(*args):
    try:
        #confirm key-value pair
        if len(args) % 2 != 0:
            return {"Error": "MSET needs to have key - value pair"}
        
        for i in range(0, len(args), 2):
            key = args[i]
            value = args[i + 1] #value is the item after key
            store[key] = value

        return {"SUCCESS": "Added all data successfully"}
    
    except Exception as e:
        return {"Error":f"MSET failed: {str(e)}"}    

#get
def handle_get(*args):
    try:
        #need just key
        if len(args) != 1:
            return {"Error": "GET needs only 1 arg"}
        
        key = args[0]

        if key in store:
            return {"value": store[key]}
        else:
            return {"Error": "Key not found"}
        
    except Exception as e:
        return {"Error":f"GET failed: {str(e)}"}
    
#multiple get
def handle_mget(*args):
    try:
        # atleast 1 or more keys
        if len(args) < 1:
            return {"Error": "MGET can't have less than 1 arg"}
        
        value = [] #store value of keys
        for key in args: 
            value.append(store.get(key, None))

        return {"values": value}    
    
    except Exception as e:
        return {"Error":f"MGET failed: {str(e)}"}
         
# delete
def handle_delete(*args):
    try:
        #need key
        if len(args) != 1:
            return {"Error": "DEL needs only 1 arg"}
        
        key = args[0]
        #pop only if key is present
        if key in store:
            store.pop(key)
            return {"SUCCESS": " Data deleted successfully"}
        else:
            return {"Error":"Couldn't find Key"}
        
    except Exception as e:
        return {"Error":f"DEL failed: {str(e)}"}

#key exist
def handle_exist(*args):
    try:
        #needs only key
        if len(args) != 1:
            return {"Error": "EXIST needs only 1 arg"}
        
        key = args[0]

        if key in store:
            return {"msg":"Key is present"}
        else:
            return {"Error": "Key not found"}
        
    except Exception as e:
        return {"Error": f"EXIST failed: {str(e)} "} 

#clear data
def handle_flushall():
    try:
        #flush only if store is not empty
        if store:
            store.clear()
            return {"SUCCESS": "Cleared storage succesfully"}
        else:
            return {"Error": "Storage is empty"}
        
    except Exception as e:
        return {"Error": f"FLUSHALL failed: {str(e)}"}

# keys present
def handle_returnkeys():
    try:

        if store:
            return {"keys": list(store.keys())} #return the keys present
        else:
            return {"Error": "Storage is empty"}
        
    except Exception as e:
        return {"Error": f"KEYS failed: {str(e)}"}    

# append to existing key
def handle_append(*args):
    try:
        #need key and new value to append
        if len(args) != 2:
            return {"Error": "APPEND needs 2 args"}
        
        key = args[0]
        add_value = args[1]

        #allow new keys if not present
        if key not in store:

            store[key] = ""

        #key and value must be string
        if isinstance(add_value, str) and isinstance(store[key], str):
            store[key] = store[key] + add_value
            return {"SUCCESS": "Updated key value"}
        else:
            return {"Error": "Error appending value, make sure key is valid and value is a string"}  
          
    except Exception as e:
        return {"Error": f"APPEND failed: {str(e)}"}    
    
# left push
def handle_lpush(*args):
    try:
        #needs value and key 
        if len(args) != 2:
            return {"Error": "LPUSH needs 2 args"}
        
        key = args[0]
        value = args[1]

        #allow new key if key not present
        if key not in store:
            store[key] = []

        store[key].insert(0, value)#insert left
        return {"SUCCESS": "Stored task succesfully"}
         
    except Exception as e:
        return {"Error": f"LPUSH failed: {str(e)}"}
    
#right push
def handle_rpush(*args):
    try:
        #needs value and key
        if len(args) != 2:
            return {"Error": "RPUSH needs 2 args"}
        
        key = args[0]
        value = args[1]

        if key not in store:
            store[key] = []

        store[key].append(value)#insert right
        return {"SUCCESS": "Stored task succesfully"} 
       
    except Exception as e:
        return {"Error": f"RPUSH failed: {str(e)}"}
    
# left pop
def handle_lpop(*args):
    try:

        if len(args) != 1:
            return {"Error": "LPOP needs only 1 arg"}
        
        key = args[0]

        
        if key in store and store[key]:
            store[key].pop(0)
            return {"SUCCESS: Task deleted successfully"}
        else:
            return {"Error": "key not found or list is empty"}
        
    except Exception as e:
        return {"Error": f"LPOP failed: {str(e)}"}


#right push
def handle_rpop(*args):
    try:

        if len(args) != 1:
            return {"Error": "RPOP needs only 1 arg"}
        
        key = args[0]

        if key in store and store[key]:
            store[key].pop()
            return {"SUCCESS: Task deleted successfully"}
        else:
            return {"Error": "key not found or list is empty"}
        
    except Exception as e:
        return {"Error": f"RPOP failed: {str(e)}"}
    

#length of queue
def handle_len(*args):
    try:

        if len(args) != 1:
            return {"Error": "LEN needs only 1 arg"}
        
        key = args[0]

        if key in store:
            return {"Length": len(store[key])}
        else:
            return {"Error": "key not found"}
        
    except Exception as e:
        return {"Error": f"LEN failed: {str(e)}"}


#range
def handle_range(*args):
    try:
        #needs start, stop and the key
        if len(args) != 3:
            return {"Error": "RANGE needs 3 args"}
        
        key = args[0]
        start = int(args[1])
        stop = int(args[2])
       
        if key in store:
            values = store[key]
            range_result = values[start:stop]#range
            return {"Range": range_result}
        else:
            return {"Error": "key not found"}
        
    except Exception as e:
        return {"Error": f"RANGE failed: {str(e)}"}
    

#remove from queue
def handle_rem(*args):
    try:
        #needs key and value
        if len(args) != 2:
            return {"Error": "REMOVE needs 2 args"}
        
        key = args[0]
        value = args[1]

        if key in store:
            store[key].remove(value)#remove
            return {"SUCCESS": "Value removed from queue"}
        else:
            return {"Error": "key not found"}
        
    except Exception as e:
        return  {"Error": f"REMOVE failed: {str(e)}"}


 
import redis
import redis.exceptions as redisError

class TestRedis:


    """ Main initialization function to establish the connection to Redis """
    def __init__(self,host,port):
        try:
            self.con = redis.Redis(host=host,port=port,db=0)
        except redisError.ConnectionError:
            print("An error occured while connecting. Make sure the Redist server is on and working.")
            raise


    """ Function to list all keys set in Redis"""
    def list_all_keys(self):
        list_of_keys = (self.con.keys())
        decoded_list_of_keys = []
        for x in list_of_keys:
            decoded_list_of_keys.append(x.decode())

        if not decoded_list_of_keys:
            return "No keys are set in Redis."
        else:
            return decoded_list_of_keys



    """ Function to list all keys in a given pattern """

    def get_keys(self, pattern):
        list_of_keys = self.con.keys(pattern=pattern)
        decoded_list_of_keys = []
        for x in list_of_keys:
            decoded_list_of_keys.append(x.decode())
        if not decoded_list_of_keys:
            return "No keys are set in Redis."
        else:
            return decoded_list_of_keys



    """ Function to delete a given key in Redist """
    def delete_key(self,key):
        if not self.con.exists(key):
            print("Key does not exist.")
        else:
            self.con.delete(key)

    """ Function to flush and clean the database, clearing the cache and all keys. """
    def clean_database(self):
        self.con.flushall()
        print("Redis is now flushed and cleared.")

    """ Function to create a key with a value in Redist"""
    def create_key(self,key,value):
        key_value=self.get_key_value(key)
        if key_value is not None:
            print("A key with that name already exists, with value ("+key_value+").")
            return

        else:
            self.con.set(key,value)

    """ Function to return the value of a key """
    def get_key_value(self,key):
        if (self.con.exists(key)):
            key_value = self.con.get(key).decode()
            return key_value
        else:
            return

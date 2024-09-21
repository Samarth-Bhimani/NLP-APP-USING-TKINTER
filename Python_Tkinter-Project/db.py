import json

class Database:

    def Add_Data(self,name,email,password):

        try:
            with open('mydb.json' , 'r') as rf:
                database = json.load(rf)
        except FileNotFoundError:
            print("File not found. Ensure the file exists.")
            return 0
        except json.JSONDecodeError:
            print("Invalid JSON format in the file.")
            return 0
        except Exception as e:
            print(e)
            return 0

        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open('mydb.json' , 'w') as wf:
                json.dump(database,wf, indent=4)
            return 1

    def Search(self,email,password):

        try:
            with open('mydb.json', 'r') as rf:
                database = json.load(rf)
        except FileNotFoundError:
            print("File not found. Ensure the file exists.")
            return -1
        except json.JSONDecodeError:
            print("Invalid JSON format in the file.")
            return -1
        except Exception as e:
            print(e)
            return -1
        else:
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return -1

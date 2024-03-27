import os.path

message = ["Hello", "World"]
for wrd in message:
    print(wrd)

print(6.5 / 3) # regular division 
print(6.5 // 3) # int division

foo = "bar"
print(foo) # Cant do this > print(foo = "bar")
print(foo:="foo") # weird Walrun assignment operator

class PersonalRecord:
    name: str = None
    age: int = None
    job: str = None
    def __init__(self, name: str, age: int, job: str) -> None:
        self.name = name
        self.age = age
        self.job = job
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}\nJob: {self.job}\n"
    
class RecordManager:
    fileName = 'records.txt'
    allRecords: PersonalRecord = list()

    def validateRecord(func):
        def wrapper(self,pr):
            if type(pr) == PersonalRecord:
                func(self, pr)
        return wrapper    

    @validateRecord 
    def AddRecord(self, pr: PersonalRecord) -> None:
        self.allRecords.append(pr)

    def DisplayAllRecords(self) -> None:
        for pr in self.allRecords:
            print(pr)

    def WriteRecord(self, file: str, pr: PersonalRecord) -> None:
        if(os.path.exists(file)):
            with open(file, 'a') as records:
                records.write(f'{pr.name},{pr.age},{pr.job}\n')
        else:
            with open(file, 'w') as records:
                records.write(f'{pr.name},{pr.age},{pr.job}\n')
    
    def WriteAllRecords(self) -> None:
        for pr in self.allRecords:
            self.WriteRecord(self.fileName, pr)
            

# -------- TESTING --------
rm = RecordManager()
rm.AddRecord(rec:= PersonalRecord("Nabil",32,"Game Dev"))
rm.AddRecord(rec:= PersonalRecord("Jess",28,"Analyst"))
rm.AddRecord(rec:= PersonalRecord("Bob",55,"Engineer"))
rm.AddRecord(rec:= PersonalRecord("Alice",35,"Technician"))
rm.AddRecord("Steve")
rm.DisplayAllRecords()
# rm.WriteAllRecords()
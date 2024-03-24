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
        return f"Name: {self.name}\nAge: {self.age}\nJob: {self.job}"
    
def WriteRecord(file: str, record: PersonalRecord) -> None:
    with open(file, 'w') as records:
        records.write(f'{record.name},{record.age},{record.job}\n')

p1 = PersonalRecord("Nabil", 32, "Game Dev")

WriteRecord("records.txt", p1)

class RecordManager:
    allRecords: PersonalRecord = list()


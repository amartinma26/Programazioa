from pydantic import BaseModel

class ZereginBerria(BaseModel):
    izenburua: str
    egina: bool = False

class Zeregina(ZereginBerria):
    id: int


#2. egorea kodea 200
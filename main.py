from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from datetime import date
import uuid

app = FastAPI()

# Definição do modelo Pydantic com regras de validação
class Item(BaseModel):
    # nome: string com limite de 25 caracteres
    nome: str = Field(..., max_length=25)
    # valor: número decimal
    valor: float
    # data: objeto do tipo date
    data: date

    # Validação customizada: a data não pode ser futura
    @validator('data')
    def data_nao_pode_ser_futura(cls, v):
        if v > date.today():
            raise ValueError('A data deve ser menor ou igual à data atual')
        return v

@app.post("/items/")
async def create_item(item: Item):
    # Converte o modelo pydantic para um dicionário Python
    item_dict = item.dict()
    
    # Gera um UUID v4 dinamicamente e adiciona ao dicionário
    item_dict["uuid"] = str(uuid.uuid4())
    
    # Retorna o JSON completo conforme solicitado
    return item_dict

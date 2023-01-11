from typing import Union
from fastapi import FastAPI
from operations_generator import get_generation_operations

my_own_api = FastAPI()


@my_own_api.get("/")
async def root():
    return {"messages": "hello"}


@my_own_api.get("/operations/{count_primes}")
async def noroot(count_primes):
    structure_ements = get_generation_operations(count_primes)
    return structure_ements

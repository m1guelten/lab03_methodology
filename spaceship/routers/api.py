from fastapi import APIRouter
import numpy as mt

router = APIRouter()


@router.get('')
# def hello_world() -> dict:
#     return {'msg': 'Hello, World!'}

def matrix() -> dict:
    matrix_a = mt.random.rand(10,10)
    matrix_b = mt.random.rand(10,10)

    product = mt.dot(matrix_a,matrix_b)
    result = {
        "matrix_a":matrix_a.tolist(),
        "matrix_b":matrix_b.tolist(),
        "product":product.tolist()
    }
    return result
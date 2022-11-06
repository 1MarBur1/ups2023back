from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def caesar(plainText: str, shift: int) -> str: 
	cipherText = ''
	for ch in plainText:
		if ch.isalpha():
			stayInAlphabet = ord(ch) + shift 
			if stayInAlphabet > ord('z'):
				stayInAlphabet -= 26
			finalLetter = chr(stayInAlphabet)
			cipherText += finalLetter
	return cipherText

class EncodeBody(BaseModel): 
	message: str
	rot: int

@app.get('/')
def root():
	return {'message': 'Hello, Hitagi'}

@app.post('/encode')
def encode(body: EncodeBody):
	return {'message': caesar(body.message, body.rot)}

@app.get('/decode')
def decode(message: str, rot: int):
	return {'message': caesar(message, -rot)}
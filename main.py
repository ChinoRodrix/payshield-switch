from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import Optional

app = FastAPI(title="PayShield Switch", description="ISO8583 message parser and builder for simulation purposes", version="0.1.0")

class ISO8583ParseRequest(BaseModel):
    message: str

class ISO8583BuildRequest(BaseModel):
    mti: str
    f2: Optional[str] = None
    f3: Optional[str] = None
    f4: Optional[str] = None
    f11: Optional[str] = None
    f37: Optional[str] = None
    f39: Optional[str] = None

    @validator('mti')
    def validate_mti(cls, v):
        if len(v) != 4 or not v.isdigit():
            raise ValueError("MTI must be a 4-digit string")
        return v

@app.post("/parse")
def parse_iso8583(req: ISO8583ParseRequest):
    msg = req.message
    if len(msg) < 20:
        raise HTTPException(status_code=400, detail="Message too short to parse")

    # For simplicity, assume fields at fixed positions (not full spec)
    mti = msg[:4]
    f2 = msg[4:24].lstrip('0') or None
    f3 = msg[24:30] or None
    f4 = msg[30:42] or None
    f11 = msg[42:48] or None
    f37 = msg[48:60] or None
    f39 = msg[60:62] or None

    return {"mti": mti, "f2": f2, "f3": f3, "f4": f4, "f11": f11, "f37": f37, "f39": f39}

@app.post("/build")
def build_iso8583(req: ISO8583BuildRequest):
    mti = req.mti
    f2 = (req.f2 or "").zfill(20)
    f3 = (req.f3 or "").ljust(6, "0")
    f4 = (req.f4 or "").ljust(12, "0")
    f11 = (req.f11 or "").ljust(6, "0")
    f37 = (req.f37 or "").ljust(12, "0")
    f39 = (req.f39 or "").ljust(2, "0")

    message = f"{mti}{f2}{f3}{f4}{f11}{f37}{f39}"
    return {"message": message}

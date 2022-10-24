from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from pydantic import BaseModel
from typing import List, Optional
from utils import save_image


app = FastAPI(root_path="/11JeG4qloFPsP8ZA3Pm--alf8K-LVUh5plAlMV42HD-p6VoJiZXEX_2YVoKUqTLR/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


class GenImage(BaseModel):
    prompt : str
    guidance_scale: Optional[float] = 7.5

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")

@app.post("/genimage")
def gen_image(req:GenImage):
    with autocast("cuda"):
        img = pipe(req.prompt,guidance_scale=req.guidance_scale).images[0]
        img_url,fname = save_image(img)
    return{'url':img_url}

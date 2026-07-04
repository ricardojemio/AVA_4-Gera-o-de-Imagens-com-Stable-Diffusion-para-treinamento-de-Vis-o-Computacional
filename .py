import time
import torch
from diffusers import StableDiffusionPipeline

# 1. Inicialização do pipeline otimizado para GPU (CUDA)
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

# 2. Definição do prompt e marcação temporal inicial
ti = time.time()
prompt = "Rocky Martian landscape with deep craters, sharp volcanic rocks, steep cliffs, red dust storm in the distance, high resolution planetary exploration view"

# 3. Inferência e geração da imagem
image = pipe(prompt).images[0]

# 4. Salvamento e exibição do resultado
image.save("output.png")
image.show()

# 5. Cálculo do tempo total de execução (tt)
tf = time.time()
tt = tf - ti
print(f"Tempo de execução (tt): {tt:.4f} segundos")

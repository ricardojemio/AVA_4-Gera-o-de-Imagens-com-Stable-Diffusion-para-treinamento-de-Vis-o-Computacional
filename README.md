# 🤖 Geração de Dados Sintéticos com Stable Diffusion v1-5

[cite_start]Este repositório contém o script de laboratório desenvolvido para a disciplina **Sistemas Evolutivos e Aplicados à Robótica** (UNIJORGE / UVA)[cite: 1, 2]. [cite_start]O objetivo do projeto é avaliar a eficiência e as limitações do modelo latente de difusão **Stable Diffusion v1-5** na criação de cenários virtuais para o treinamento de sensores visuais e algoritmos de visão computacional em robôs adaptativos[cite: 7, 8, 9].

## 🚀 Como Executar

[cite_start]O código foi projetado para rodar em ambiente **Google Colab** utilizando aceleração por GPU de modo a otimizar a velocidade de inferência[cite: 9].

### 1. Pré-requisitos
Instale as dependências necessárias do ecossistema Hugging Face:
```bash
pip install diffusers transformers torch

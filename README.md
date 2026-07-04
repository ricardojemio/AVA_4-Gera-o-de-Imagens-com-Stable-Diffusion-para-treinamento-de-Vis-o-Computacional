# 🤖 Geração de Dados Sintéticos com Stable Diffusion v1-5

Este repositório contém o script de laboratório desenvolvido para a disciplina **Sistemas Evolutivos e Aplicados à Robótica** 
O objetivo do projeto é avaliar a eficiência e as limitações do modelo latente de difusão **Stable Diffusion v1-5** na criação de cenários virtuais para o treinamento de sensores visuais e algoritmos de visão computacional em robôs adaptativos.

## 🚀 Como Executar

O código foi projetado para rodar em ambiente **Google Colab** utilizando aceleração por GPU de modo a otimizar a velocidade de inferência.

### 1. Pré-requisitos
Instale as dependências necessárias do ecossistema Hugging Face:
```bash
pip install diffusers transformers torch

# 🤖 Geração de Dados Sintéticos com Stable Diffusion v1-5

Este repositório contém o script de laboratório desenvolvido para a disciplina **Sistemas Evolutivos e Aplicados à Robótica**.O objetivo do projeto é avaliar a eficiência e as limitações do modelo latente de difusão **Stable Diffusion v1-5** na criação de cenários virtuais para o treinamento de sensores visuais e algoritmos de visão computacional em robôs adaptativos.

---

## 📊 Resultados e Benchmarks de Desempenho

O pipeline foi testado com 6 abordagens conceituais diferentes (cenários de exploração espacial vs. testes de estresse com objetos e animais).

* **Média Geral de Inferência:** ~11.54 segundos por imagem (512x512 pixels).

| ID do Teste | Prompt de Entrada (Resumo) | Tempo ($tt$) | Diagnóstico de Consistência Visual |
| :---: | :--- | :---: | :--- |
| **01** | Cenário Marciano / Exploração Espacial | 11.68 s | **Sucesso Total:** Geração de imagem correta. |
| **02** | Gato comendo cheeseburger em mesa | 9.83 s | **Omissão Semântica:** O gato foi omitido (*catastrophic forgetting*) pela saturação do cenário de fast-food. |
| **03** | Capivara usando chapéu de chef | 12.59 s | **Falha de Adereço:** Boa textura animal, mas ignorou o chapéu solicitado. |
| **04** | Pug gamer com fone sob luz neon | 11.95 s | **Sucesso de Fusão:** Boa integração geométrica mas gerou de forma icorreta o fone de ouvido. |
| **05** | Pinguim relaxando na praia de óculos | 10.96 s | **Alucinação Espacial:** Quebra da física de camadas (duplicou os óculos e fundiu elementos). |
| **06** | Golden retriever com lupa na boca | 12.22 s | **Anomalia Mecânica:** O cabo da lupa fundiu-se ao focinho, revelando falta de lógica de física 3D do modelo. |

---

## 🧠 Principais Aprendizados (Visão Computacional)

* **Previsibilidade Computacional:** O tempo de processamento é praticamente constante ($\approx 11.5\text{ s}$) e não é afetado pela quantidade de texto digitada no prompt.
* **Limitação Física 3D:** Modelos de difusão de base operam via correlação estatística bidimensional de pixels. Eles não entendem mecânica tridimensional (ex: o ato físico de segurar algo), gerando alucinações estruturais perigosas para treinamento robótico de precisão se não forem filtrados ou controlados via *ControlNet* ou *LoRA*.

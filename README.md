# Menu Interativo da Câmera Jovi

Projeto acadêmico de Engenharia de Software: um menu interativo de terminal, escrito em Python, que apresenta os modos de uma câmera para a empresa **Jovi** (conhecida como Vivo no exterior). A versão atual inclui uma consulta de condições climáticas em tempo real, obtidas de uma API pública, para ajudar a decidir como fotografar.

## Informações do projeto

- **Disciplina:** Computational Thinking with Python
- **Instituição:** FIAP
- **Professor(a):** Helder Faria Andriolo
- **Integrantes:**
  - Eduardo de Abreu Gouvêa         - RM573414
  - Felipe Roberto Cassiano         - RM569238
  - Paulo Henrique Moreira Angueira - RM573245
  - Vinícius Mansur Magalhães       - RM571518

## Funcionalidades

O programa abre um menu no terminal com as seguintes opções:

| Opção | Nome | O que faz |
|-------|------|-----------|
| 1 | Modo Pet | Descreve o modo que tira fotos automáticas de pets quando a câmera estabiliza e reconhece o animal. |
| 2 | Modo Documento | Descreve o modo que escaneia textos e os envia para a área de transferência do celular. |
| 3 | Modo Live Suggestions | Descreve o modo que analisa a cena e sugere ajustes nas configurações da câmera. |
| 4 | Histórico | Mostra quantas opções foram acessadas na sessão e quais foram. |
| 5 | Gráficos | Exibe gráficos de barras com os resultados da pesquisa de aceitação dos modos. |
| 6 | Condições para Foto | Consulta o clima da cidade informada e sugere ajustes para fotografar. |
| 0 | Sair | Encerra o programa. |

### Opção 6: Condições para Foto

O usuário digita o nome de uma cidade. O programa busca as coordenadas dela, consulta as condições atuais e exibe os valores que mais influenciam a qualidade de uma foto, junto com uma sugestão para cada um:

| Condição | Limite que gera aviso | Sugestão |
|----------|-----------------------|----------|
| Cobertura de nuvens | 80% ou mais | Aumentar o ISO ou usar o modo HDR |
| Índice UV | 8 ou mais | Evitar fotografar de frente para o Sol ou usar o modo HDR |
| Precipitação | Maior que 0 | Proteger o celular da chuva |
| Visibilidade | Menos de 1000 m | Aumentar o ISO ou usar o modo HDR |

### Gráficos (opção 5)

Os gráficos usam os dados fixos da pesquisa de aceitação realizada com os participantes:

1. Aceitação dos modos
2. Modo Documento por faixa etária
3. Aceitação do Live Suggestions
4. Aceitação do Modo Pet

## API utilizada

A opção 6 usa duas APIs gratuitas da **[Open-Meteo](https://open-meteo.com/)**, que não exigem cadastro nem chave de acesso:

- **Geocoding API**: transforma o nome da cidade em latitude e longitude.
- **Forecast API**: devolve as condições atuais (nuvens, índice UV, precipitação, visibilidade e rajadas de vento) e os horários de nascer e pôr do sol.

Os dados meteorológicos são fornecidos pela Open-Meteo, sob licença CC BY 4.0.

## Requisitos

- **Python 3.10 ou superior** (o código usa `match/case`)
- Bibliotecas externas:
  - `requests`
  - `matplotlib`
- Conexão com a internet (apenas para a opção 6)

As demais bibliotecas usadas (`os` e `time`) já vêm com o Python.

## Instalação

1. Confira a versão do Python:

   ```bash
   python --version
   ```

2. Instale as bibliotecas:

   ```bash
   pip install requests matplotlib
   ```

   Em alguns sistemas, o comando pode ser `pip3` em vez de `pip`.

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

Substitua `main.py` pelo nome do arquivo do projeto, se for diferente. Em alguns sistemas, o comando pode ser `python3`.

Depois, digite o número da opção desejada e pressione Enter. Em cada tela, digite qualquer coisa para voltar ao menu.

## Limitações conhecidas

- A opção 6 precisa de internet. Sem conexão, a consulta não funciona.
- A busca de cidades está restrita ao **Brasil** (`countryCode=BR`).
- A consulta mostra apenas as condições do momento atual, sem previsão para outros horários.
- Se a cidade digitada não for encontrada ou houver falha na API, o programa pode encerrar com erro.
- Os modos Pet, Documento e Live Suggestions são apenas descritivos: não há câmera real integrada.
- Os dados dos gráficos são fixos, vindos da pesquisa, e não se atualizam.
- Os gráficos abrem em janelas do `matplotlib`, e o menu só continua depois que a janela é fechada.

## Créditos

- Dados meteorológicos: [Open-Meteo](https://open-meteo.com/)
- Desenvolvido por: Eduardo de Abreu Gouvêa, Felipe Roberto Cassiano, Paulo Henrique Moreira Angueira e Vinícius Mansur Magalhães
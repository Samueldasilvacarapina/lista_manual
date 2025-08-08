import streamlit as st

def extrair_nomes(texto):
    linhas = texto.strip().split('\n')

    nomes = []
    meses = ['janeiro', 'fevereiro', 'março', 'marco', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',
             'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    palavras_ignoradas = ['Observadores', 'Documentação', 'vox,', 'vinicius', 'trindade']

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            continue
        if linha.startswith('R$'):
            continue
        primeiro_token = linha.split()[0].lower()
        if primeiro_token[0].isdigit():
            continue
        if primeiro_token in meses:
            continue
        if '+ Atividade' in linha:
            continue
        if linha.isdigit():
            continue
        if any(palavra.lower() in linha.lower() for palavra in palavras_ignoradas):
            continue
        if len(linha.split()) >= 2:
            nomes.append(linha)

    # Adiciona numeração
    nomes_numerados = [f"{i+1} - {nome}" for i, nome in enumerate(nomes)]
    return '\n'.join(nomes_numerados)

st.title("Extrator de Nomes")

texto_entrada = st.text_area("Cole seu texto aqui", height=400)

if st.button("Extrair Nomes"):
    if texto_entrada.strip():
        resultado = extrair_nomes(texto_entrada)
        st.text_area("Nomes extraídos:", resultado, height=400)
    else:
        st.warning("Por favor, cole o texto no campo acima.")

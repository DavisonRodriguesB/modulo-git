"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Reque..
- Repetir o processo até concluir todas as funções...

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():

    return "Bem-vindo ao Desafio de Git!"

def listar_comandos_git_basicos():
    
    return ["git init", "git add", "git commit", "git status", "git push"]


def criar_mensagem_commit(funcao_nome):
    
    return f"Implementa função {funcao_nome}"


def verificar_tag_valida(tag):
    import re
    return bool(re.fullmatch(r"v\d+\.\d+", tag))


def gerar_relatorio_final(funcoes_concluidas):
    quantidade = len(funcoes_concluidas)
    return f"Desafio concluído! {quantidade} funções implementadas com sucesso."


"""LAB FINAL"""
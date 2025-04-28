# Criando um dicionário de contatos
contatos = {
    "Ana": "555-1234",
    "Pedro": "555-5678",
    "Maria": "555-8765"
}

# Adicionando um novo contato
contatos["Lucas"] = "555-4321"

# Acessando um número de telefone
telefone_ana = contatos.get("Ana")
print("Número de Ana:", telefone_ana)

# Removendo um contato
contatos.pop("Pedro")
print("Contatos após remoção de Pedro:", contatos)

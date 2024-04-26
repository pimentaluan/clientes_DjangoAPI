# Clientes com Django API 📝🔍

Neste repositório, desenvolvi uma API de clientes utilizando o Django REST Framework. Cada cliente possui os seguintes atributos:
- Nome
- Email
- CPF
- RG
- Celular
- Ativo

Durante o curso, aprendi a validar o serializer, importar e gerar clientes através de um script, além de trabalhar com recursos avançados, como paginação, ordenação, busca e filtro. Também explorei o processo de deployment na AWS.

### Funcionalidades Principais:
- **Cadastro de Clientes:** Permite criar, visualizar, atualizar e excluir informações sobre os clientes.
- **Validação de Dados:** Implementei validações para garantir a integridade dos dados, como a unicidade do CPF.
- **Importação de Clientes:** Desenvolvi um script para importar e gerar clientes automaticamente.
- **Recursos Avançados:** Utilizei recursos avançados do Django REST Framework, como paginação, ordenação, busca e filtro.
- **Deploy na AWS:** Realizei o deployment da API na AWS, permitindo o acesso remoto aos dados dos clientes.

### Utilização:
1. **Clonar o Repositório:**
    ```
    git clone https://github.com/pimentaluan/clientes_DjangoAPI.git
    ```

2. **Instalar Dependências:**
    ```
    cd clientes_DjangoAPI
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Configurar o Banco de Dados:**
    Certifique-se de configurar as credenciais do banco de dados no arquivo de configuração `settings.py`, e execute as migrações:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Executar o Servidor:**
    ```
    python manage.py runserver
    ```

A API estará disponível em:
```
http://localhost:8000/
```

ou, se ainda estiver no prazo:
```
http://18.231.168.125:8000/clientes/
```

### Observação sobre o Deploy:
O link para o deploy pode estar disponivel temporariamente devido às limitações do plano da AWS, que possui um limite de tempo.

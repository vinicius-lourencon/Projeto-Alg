# Sistema de Gerenciamento Acadêmico

## Descrição
O **Sistema de Gerenciamento Acadêmico** é uma aplicação desenvolvida em Python para facilitar a gestão de alunos, professores, disciplinas e turmas em uma instituição de ensino. Ele oferece funcionalidades como cadastro de usuários, alocação de professores, matrícula de alunos e visualização de turmas.

## Estrutura do Projeto
O sistema é modularizado, com funcionalidades separadas em diferentes arquivos para melhorar a organização e manutenção do código. Os módulos incluem:

- **cadastrar_aluno.py**: Lida com o cadastro de alunos.
- **cadastrar_professor.py**: Lida com o cadastro de professores.
- **cadastrar_disciplina.py**: Gerencia o cadastro de disciplinas.
- **cadastrar_turma.py**: Gerencia o cadastro de turmas.
- **alocar_professor.py**: Permite alocar professores a disciplinas.
- **filtrar_professores.py**: Permite filtrar professores por disciplina.
- **matricular_aluno.py**: Gerencia a matrícula de alunos em turmas.
- **ver_turmas.py**: Exibe informações sobre as turmas cadastradas.

O arquivo principal **projeto1.py** integra todas as funcionalidades e fornece um menu de interação para o usuário.

## Funcionalidades
1. **Cadastrar Aluno**: Adiciona novos alunos ao sistema.
2. **Cadastrar Professor**: Adiciona novos professores ao sistema.
3. **Cadastrar Disciplina**: Permite o cadastro de disciplinas, vinculando-as a professores.
4. **Cadastrar Turma**: Cria novas turmas e vincula disciplinas e professores.
5. **Alocar Professor a Disciplina**: Atribui professores às disciplinas criadas.
6. **Matricular Aluno em Turma**: Realiza a matrícula de alunos em turmas especificadas.
7. **Filtrar Professores por Disciplina**: Filtra professores com base nas disciplinas atribuídas.
8. **Ver Turmas**: Exibe todas as turmas com suas respectivas disciplinas, professores e alunos.

## Requisitos
- Python 3.8 ou superior

## Como Executar
1. Certifique-se de ter todos os módulos mencionados na mesma pasta do arquivo principal (**projeto1.py**).
2. Execute o arquivo **projeto1.py** com o comando:
   ```bash
   python projeto1.py
   ```
3. Utilize o menu para interagir com o sistema.

## Exemplo de Uso
- Ao iniciar, o sistema exibirá um menu com as opções numeradas.
- Escolha a opção desejada inserindo o número correspondente e seguindo as instruções na tela.

## Observações
- Certifique-se de tratar qualquer erro ou exceção que possa ocorrer durante o uso do sistema.
- Os dados inseridos durante a execução do programa não serão salvos permanentemente.

## Autor
Vinicius Antonio Lourençon  
Discente do curso de TADS no IFMS - Campus Três Lagoas


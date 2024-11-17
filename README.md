# sistemagerenciamentoalunos

 
 Atividade: Sistema de Gerenciamento de Alunos
Crie um programa em Python que gerencie uma lista de alunos. O programa deve oferecer as seguintes opções:

1. Cadastrar novo aluno:
   - O usuário insere o nome e a nota do aluno.
   - Certifique-se de que o nome do aluno não esteja vazio e que a nota seja um número válido entre 0 e 10.
   - Armazene os alunos em uma lista no formato:
     ```python
     {'nome': 'João', 'nota': 8.5, 'aprovado': True}
     ```
     A chave `'aprovado'` será calculada automaticamente (nota maior ou igual a 6).
     
2. Listar todos os alunos:
   - Mostre uma tabela com o nome, nota e status de aprovação (`Aprovado` ou `Reprovado`).

3. Atualizar a nota de um aluno:
   - Peça o nome do aluno.
   - Atualize a nota do aluno caso ele exista, e recalcule o status de aprovação.

4. Excluir um aluno:
   - Peça o nome do aluno e remova-o da lista, se existir.

5. Sair do programa:
   - Finalize o programa com uma mensagem de despedida.

---

 Regras e Dicas
1. Use funções:
   - Cada funcionalidade (como cadastro, listagem, etc.) deve ser implementada em uma função separada.
2. Validação:
   - Verifique entradas inválidas (ex.: notas fora do intervalo 0-10, nome vazio).
3. Organização:
   - Use subtítulos e limpe a tela entre as ações, como no código fornecido.
4. Estrutura de repetição:
   - O programa deve exibir o menu até o usuário escolher sair.

---

 Exemplo de saída esperada

 Menu Principal
```
██████████████████████████████████
       GERENCIAMENTO DE ALUNOS
██████████████████████████████████

1. Cadastrar novo aluno
2. Listar todos os alunos
3. Atualizar nota de um aluno
4. Excluir um aluno
5. Sair
Escolha uma opção: _
```

 Listagem
```
NOME                    | NOTA   | STATUS
------------------------------------------------
João                    | 8.5    | Aprovado
Maria                   | 5.0    | Reprovado
```

 Mensagens interativas
- Ao cadastrar:
  ```
  O aluno Pedro foi cadastrado com sucesso!
  ```
- Ao atualizar:
  ```
  A nota de João foi atualizada para 9.0. Status: Aprovado
  ```
- Ao excluir:
  ```
  O aluno Maria foi excluído com sucesso.
  ```

---

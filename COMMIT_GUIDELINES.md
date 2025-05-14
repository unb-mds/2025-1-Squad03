# 📘 Guia de Padrões de Commit

Este documento define as diretrizes para mensagens de commit no projeto, seguindo a especificação do [Conventional Commits](https://www.conventionalcommits.org/).

---

## 📐 Estrutura da Mensagem de Commit


- **tipo**: Categoria da mudança no código.
- **escopo** *(opcional)*: Parte do projeto afetada (ex: `auth`, `api`, `login`, `header`, etc).
- **descrição**: Frase curta, imperativa, descrevendo o que foi feito.

---

## 🧩 Tipos de Commit com Exemplos de Escopo

| Tipo       | Descrição                                              | Exemplos de Escopo             |
|------------|--------------------------------------------------------|--------------------------------|
| `feat`     | Adição de nova funcionalidade                          | `login`, `dashboard`, `api`    |
| `fix`      | Correção de bug                                        | `form`, `auth`, `profile`      |
| `docs`     | Alterações na documentação                             | `readme`, `guia`, `contributing` |
| `style`    | Mudanças visuais ou de formatação                      | `header`, `footer`, `layout`   |
| `refactor` | Refatoração sem alterar comportamento                  | `auth`, `hooks`, `services`    |
| `perf`     | Melhorias de desempenho                                | `db`, `render`, `api`          |
| `test`     | Adição ou modificação de testes                        | `user`, `auth`, `api`          |
| `build`    | Mudanças no sistema de build ou dependências           | `vite`, `webpack`, `deps`      |
| `ci`       | Configuração de integração contínua                    | `github`, `vercel`, `actions`  |
| `chore`    | Tarefas diversas, sem impacto direto no código         | `lint`, `env`, `scripts`       |
| `revert`   | Reversão de commits anteriores                         | escopo do commit revertido     |

---

## 📝 Exemplos Completos

- `feat(login): adiciona validação de email`
- `fix(api): corrige status code na rota de logout`
- `docs(readme): inclui badges de build`
- `style(header): ajusta espaçamento e cores`
- `refactor(auth): isola lógica de verificação de token`
- `perf(database): melhora performance da query de busca`
- `test(user): cria testes unitários para cadastro`
- `build(vite): configura aliases de importação`
- `ci(github): adiciona workflow de testes automáticos`
- `chore(lint): aplica novo padrão de eslint`
- `revert: reverte commit 5f3e1a2 (auth: troca de hash)`

---

## ⚠️ Notas Importantes

- Use frases curtas no **modo imperativo** (ex: "adiciona", "remove", "corrige").
- O escopo ajuda a localizar rapidamente onde foi feita a mudança.
- Para mudanças que **quebram compatibilidade**, adicione um rodapé assim:


---

## 📚 Recursos Adicionais

- Artigo de referência: [Conventional Commits Pattern – Medium](https://medium.com/linkapi-solutions/conventional-commits-pattern-3778d1a1e657)
- Especificação oficial: [conventionalcommits.org](https://www.conventionalcommits.org/)

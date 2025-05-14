# Guia de Contribuição

Obrigado pelo seu interesse em contribuir para este projeto! Suas contribuições são muito bem-vindas e nos ajudam a melhorar continuamente.

Este guia tem como objetivo fornecer um passo a passo básico para que você possa contribuir de forma eficaz.

## Como Contribuir

1.  **Reportar Issues:**
    * Se você encontrar algum bug, tiver alguma sugestão de melhoria ou quiser propor uma nova funcionalidade, por favor, abra uma nova issue.
    * Ao criar uma issue, seja o mais claro e detalhado possível. Inclua os passos para reproduzir o problema (se aplicável), o comportamento esperado e o comportamento real.

2.  **Fork o Repositório:**
    * Faça um fork do repositório para a sua conta do GitHub.

3.  **Clone o Repositório Forkado:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
    cd NOME_DO_REPOSITORIO
    ```
    * Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub e `NOME_DO_REPOSITORIO` pelo nome do seu fork.

4.  **Crie um Branch para sua Contribuição:**
    * Crie um branch dedicado para as suas alterações. Isso ajuda a manter o seu branch principal limpo e facilita a revisão.
    ```bash
    git checkout -b nome-do-seu-branch
    ```
    * Escolha um nome de branch descritivo que reflita a sua contribuição (por exemplo, `fix-bug-login`, `add-feature-xyz`).

5.  **Faça suas Alterações:**
    * Implemente as alterações ou adicione o novo recurso.
    * Siga as convenções de código do projeto (se houver).

6.  **Commite suas Alterações:**
    * Faça commits com mensagens claras e concisas que expliquem o que foi alterado.
    ```bash
    git add .
    git commit -m "Breve descrição da sua alteração"
    ```
    * Se o seu commit resolver uma issue específica, você pode referenciá-la na mensagem do commit usando `#NUMERO_DA_ISSUE` (por exemplo, `Fix: corrige problema de login #123`).

7.  **Faça Push para o seu Repositório Forkado:**
    ```bash
    git push origin nome-do-seu-branch
    ```

8.  **Crie um Pull Request (PR):**
    * No seu repositório forkado no GitHub, clique no botão "Contribute" e depois em "Open pull request".
    * Compare o seu branch com o branch principal do repositório original.
    * Forneça um título claro e uma descrição detalhada do seu pull request. Explique o que a sua contribuição faz e o porquê.
    * Se houver alguma issue relacionada, mencione-a no seu PR.

9.  **Aguarde a Revisão:**
    * Os mantenedores do projeto irão revisar o seu pull request. Esteja aberto a receber feedback e fazer as alterações necessárias.

10. **Após a Revisão:**
    * Se o seu pull request for aprovado, ele será mergeado no branch principal. Parabéns, sua contribuição foi aceita!

## Diretrizes Gerais

* Seja respeitoso e colaborativo em todas as suas interações.
* Escreva código limpo e bem comentado.
* Tente seguir os padrões de código existentes no projeto.
* Escreva testes para suas alterações, se aplicável.
* Mantenha seus pull requests focados em uma única alteração lógica. Pull requests grandes e com muitas alterações podem ser mais difíceis de revisar.

Agradecemos novamente a sua disposição em contribuir!

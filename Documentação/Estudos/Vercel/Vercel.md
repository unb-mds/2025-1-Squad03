# Vercel (Hosteamento gratuito de sites)

## O que é Vercel?
A Vercel é uma plataforma de hospedagem e implantação de aplicações web, focada principalmente em projetos frontend, como Next.js, React, Vue.js e outras tecnologias modernas.
Ela oferece **deploy automático** a partir de repositórios do GitHub, GitHub, Bitbucket, escabilidade automática e integração com diversas ferramentas.

## Conceitos Essenciais

### Deploy
Processo de enviar e disponibilizar um site/aplicação em um servidor para que outras pessoas possam acessá-lo.

**Como fazer um deploy na Vercel?**

1. Instale a CLI da Vercel
   - Comando:  `npm install -g vercel`

2. Faça login:
   - Comando: `vercel login`

3. Dentro do diretório do seu projeto, execute:
   - Comando `vercel`

4. 


### CI/CD (Continuous Integration/Continuous Deployment)
Automação do processo de biuld, teste e deploy do código a cada atualização.
- A Vercel **já faz isso automaticamente** ao conectar um repositório
- Toda vez que você fizer um `git push`, a Vercel:
  - Executa um novo biuld.
  - Roda testes (se configurados).
  - Faz deploy em produção (ou preview).
 
### Preview Deployment
Um link temporário para testar mudanças antes de ir para produção.

**Como fazer?**
  - A Vercel gera automaticamente um preview para cada:
    - Pull Request no GitHub.
    - Commit em branches não-principais (ex: `git push origin feature/nova-pagina`).
  - Você pode compartilhar esse link com usa equipe para revisão.
 
### Production Deployment
Versão final do site (acessível pelo domínio principal).

**Como fazer?**

- Merge no branch principal (`main` ou `master`), a Vercel faz deploy automático em produção.
- Ou promova manualmente um preview para produção no painel da Vercel.






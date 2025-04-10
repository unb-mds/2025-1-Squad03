# 📘 Documentação de Requisitos

---

## ✅ Requisitos Funcionais

1. O sistema deve permitir que o usuário faça login e salve suas simulações.  
2. O sistema deve permitir upload do histórico em PDF.  
3. O sistema deve ler o PDF e identificar as disciplinas cursadas, aprovadas e reprovadas.  
4. O sistema deve consultar um banco de dados com o fluxograma do curso e equivalências.  
5. O sistema deve mostrar o fluxograma do curso do usuário com:
   - Disciplinas cursadas destacadas.  
   - Equivalências ao passar o mouse/clicar.  
   - Número de vezes que cursou/reprovou.  
6. O sistema deve calcular e exibir a porcentagem de conclusão do curso.  
7. O sistema deve permitir que o usuário informe horários não disponíveis.  
8. O sistema deve gerar automaticamente uma grade horária possível com base nas matérias disponíveis e nos horários livres.  
9. O sistema deve gerar um PDF da simulação da nova grade.  
10. O sistema deve permitir ver trocas de curso e o quanto de aproveitamento seria possível.  
11. O sistema deve armazenar os dados do usuário e simulações anteriores (se logado).  
12. O sistema deve permitir visualizar o número de semestres cursados e os restantes com base no tempo máximo do curso.  
13. O sistema deve permitir a simulação de grade de acordo com metas (ex: formar em X semestres).  
14. O sistema deve permitir que o usuário selecione preferências de grade (evitar manhãs, concentrar em poucos dias, etc).  
15. O sistema deve identificar e exibir, com base no histórico:
   - Se o aluno já trancou algum período.  
   - Quantas vezes trancou o curso.  
   - O(s) semestre(s) do(s) trancamento(s).  
16. O sistema deve identificar e exibir, com base no histórico:
   - Se o aluno trocou de curso.  
   - Qual era o curso anterior.  
   - Quando a mudança ocorreu.  
   - Quais disciplinas foram aproveitadas.  

---

## ⚙️ Requisitos Não Funcionais

1. **Responsividade:**  
   O sistema deve ser responsivo e funcionar bem em dispositivos móveis e desktop.

2. **Tempo de resposta:**  
   O sistema deve ter tempo de resposta inferior a 2 segundos para ações principais:
   - Geração de simulação de grade  
   - Exibição do fluxograma  
   - Upload e leitura de histórico

3. **Segurança de dados:**  
   - Autenticação segura para usuários logados.  
   - Dados pessoais e acadêmicos armazenados de forma criptografada.

4. **Precisão na leitura do histórico:**  
   O sistema deve garantir acurácia mínima de 95% na extração de dados dos históricos em PDF.

5. **Escalabilidade:**  
   Deve ser capaz de suportar grande número de acessos simultâneos, especialmente durante períodos de matrícula.

6. **Compatibilidade de navegador:**  
   Compatível com os navegadores:
   - Google Chrome  
   - Mozilla Firefox  
   - Microsoft Edge  
   - Safari (opcional)

7. **Usabilidade:**  
   Interface intuitiva, visual e de fácil uso, com foco em clareza e organização.

8. **Padrão visual do PDF exportado:**  
   PDF gerado deve ter layout limpo e padronizado com identidade visual do projeto.

9. **Disponibilidade:**  
   O sistema deve estar disponível 24/7 com até 0,5% de indisponibilidade mensal.

10. **Performance do parser de PDF:**  
   A leitura deve ser concluída em até 5 segundos para arquivos com até 10 páginas.

11. **Acessibilidade:**  
   O sistema deve seguir práticas básicas de acessibilidade:
   - Contraste adequado  
   - Navegação por teclado  
   - Textos alternativos

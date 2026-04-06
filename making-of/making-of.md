
# Making Of — Portfolio
 
## 1. Introdução
> Este ficheiro consiste em guiar pelo processo de criação deste projeto - portfolio.
 
---
 
## 2. Diagrama Entidade-Relacionamento (DER)
 
![DER v1](/making-of/images/modeloER.jpeg)

 
---


## 2.1 Entidades e Atributos

### Licenciatura
- nome
- duração (anos)
- url site
- objetivos

### Unidade Curricular
- nome
- ano
- semestre
- ects
- apresentação
- programa

### Docente
- nome
- email
- imagem

### Projetos
- titulo
- descrição
- url vídeo
- imagem
- conceitos
- url github
- tipo (UC / PESSOAL)

### Tecnologia
- nome
- tipo
- logo
- url site
- nível
- aspetos relevantes

### TFCs
- titulo
- aluno
- orientador
- licenciatura
- ano
- url relatório
- email
- imagem
- resumo
- áreas
- classificação 


### Competencia
- nome
- categoria

### Categoria Competencia
- nome
- descricao

### Formação
- titulo
- instituição
- data início
- data fim
- certificado

### Evento
- nome
- tipo (choices: Hackathon, Voluntariado, Competição, Conferência, Workshop, Outro)
- papel (choices: Participante, Organizador, Voluntário, Orador)
- descricao
- data
- local
- url
- imagem


### MakingOf
- entidade
- descrição
- justificação modelação
- erros
- correções
- uso IA
- fotos
 
### 2.2 Justificação das Novas Entidades
 
#### Entidade: `Projeto`
>Optei por uma única entidade "Projeto" com um atributo "tipo" para distinguir projetos de UC e pessoais. Esta abordagem evita duplicação de dados, pois ambos partilham os mesmos atributos.
 
#### Entidade: `CategoriaCompetencia`
> Considerei como entidade pois permite uma dimensão extra, ou seja, é possível adicionar novas categorias facilmente, filtrar competências por categoria de forma mais eficiente e ter um controlo mais estruturado sobre os tipos de competências existentes.
 
---
 
### 2.2 Justificação das Decisões de Modelação


### Licenciatura ↔ UnidadeCurricular (N:N)
- Uma licenciatura é composta por várias UCs. Uma UC como Fundamentos de Programação pode estar associada a vários cursos. Com N:N existe apenas um registo por UC partilhado entre cursos.


### UnidadeCurricular ↔ Docente (N:N)
- Uma UC pode ser lecionada por vários docentes (ex: teórica e prática com professores diferentes). 
- Um docente pode lecionar várias UCs ao longo do curso.
 
### UnidadeCurricular ↔ Projeto (1:N)
- A relação entre Unidade Curricular e Projeto é 1:N, sendo opcional do lado do Projeto. Isto porque apenas os projetos de UC estão associados a uma Unidade Curricular, enquanto os projetos pessoais não possuem essa associação. Embora, no meu caso, cada Unidade Curricular tenha apenas um projeto final, optei por esta modelação por permitir maior flexibilidade ao modelo
 
### Projeto ↔ Tecnologia (N:N)
- Um projeto usa várias tecnologias. 
- Uma tecnologia como Python aparece em vários projetos ao longo do curso.


### TFC ↔ Tecnologia (N:N)
- Um TFC pode utilizar várias tecnologias. 
- Uma tecnologia pode estar presente em 
vários TFCs de anos e cursos diferentes.

### Licenciatura ↔ TFC (1:N)
- Uma licenciatura tem vários TFCs associados.
- Um TFC pertence apenas a uma licenciatura.

### Competencia → CategoriaCompetencia (N:1)
- Várias competências partilham a mesma categoria (ex: Python e Django são ambas 
"técnicas"). 
- Uma competência pertence a apenas uma categoria.

### Competencia ↔ Projeto (N:N)
- Uma competência pode ser demonstrada em vários projetos. 
- Um projeto demonstra várias competências.


### Competencia ↔ Formacao (N:N)
- Uma competência pode ser adquirida em várias formações.
- Uma formação desenvolve várias competências.

### Competencia ↔ Tecnologia (N:N)
- Uma competência está frequentemente ligada a várias tecnologias e vice-versa. 

### Evento ↔ Tecnologia (N:N)
- Um evento pode usar várias tecnologias, por exemplo num hackathon 
  podem ser usadas Python, Django e React em simultâneo.
- Uma tecnologia pode estar em vários eventos, Python por exemplo 
  pode ter sido usada em vários hackathons ao longo do tempo.

### Evento ↔ Competencia (N:N)
- Um evento pode desenvolver várias competências, por exemplo num 
  hackathon desenvolvem-se competências de trabalho em equipa, 
  resolução de problemas e programação.
- Uma competência pode estar associada a vários eventos, a competência 
  "trabalho em equipa" pode ter sido desenvolvida em vários voluntariados 
  e hackathons.


### MakingOf — Relações com outras entidades

Optei por usar um campo `choices` com o nome da entidade em vez de 
ForeignKeys individuais. A abordagem com ForeignKeys ligava o registo 
a uma instância específica (ex: "Licenciatura em Engenharia Informática") 
quando o objetivo era documentar alterações ao modelo em geral 
(ex: "Licenciatura"). O campo `choices` é mais adequado porque permite 
identificar qual entidade foi afetada sem criar dependências desnecessárias, 
sendo também mais simples e flexível.

O campo choices inclui todas as entidades do projeto:
- Licenciatura, Unidade Curricular, Projeto, Tecnologia, TFC
- Competência, Categoria Competência, Formação, Evento
- MakingOf, Geral (para decisões que afetam várias entidades)
---
 
## 3. Evolução do Modelo
 ## Versão 2
 
![DER v2](/making-of/images/V2.jpeg)

**Justificação:** Os orientadores dos TFCs são docentes da Lusófona, 
pelo que faz sentido ligá-los à entidade Docente em vez de guardar 
como texto simples. Esta alteração permite relacionar TFCs com Docentes 
e futuramente adicionar mais informação sobre cada orientador.

 ## Versão 3
 
![DER v3](/making-of/images/V3.jpeg)
**Justificação:**
- Foi adicionada a entidade `Evento` para registar participações em 
hackathons, voluntariado, competições, conferências e workshops.
- Um portfólio profissional deve refletir não só o 
percurso académico mas também atividades extracurriculares. Eventos 
como hackathons e voluntariado demonstram iniciativa e trabalho em 
equipa,competências valorizadas em entrevistas de emprego.




 
---
 
## 4. Erros Identificados e Correções


---
 
## 5. Apontamentos e Notas
> **Nota:** Os registos do MakingOf foram sendo criados ao longo do 
> desenvolvimento à medida que iam surgindo erros, alterações e decisões 
> de modelação. Considerou-se mais prático registar cada ocorrência no 
> momento em que acontecia, em vez de documentar tudo no final — desta 
> forma o Making Of reflete o processo real de desenvolvimento. As 
> alterações, erros e justificações detalhadas encontram-se nos registos 
> da entidade MakingOf diretamente no projeto portfolio, tendo este 
> ficheiro servido apenas como rascunho inicial e referência de apoio.
 
---
 
## 6. Uso de IA
- ### Projetos Pessoais vs Projetos de UC 
Inicialmente, considerei separar os projetos em duas entidades distintas: projetos de Unidade Curricular e projetos pessoais. No entanto, após recorrer à IA, foi-me sugerida uma abordagem alternativa, utilizando uma única entidade `Projeto` com um atributo `tipo` para distinguir entre projetos de UC e pessoais.

Esta solução revelou-se mais adequada, uma vez que ambos os tipos de projeto partilham praticamente os mesmos atributos. A separação em duas entidades iria introduzir redundância e duplicação de estrutura no modelo.

- ### Modelação do Making of
A IA ajudou a traduzir a ideia que eu tinha em código. 
Sabia que queria um campo simples para identificar a entidade afetada, 
sem relações para instâncias específicas, mas não sabia como implementar. 
A IA sugeriu o campo `choices` que correspondia exatamente ao que pretendia.

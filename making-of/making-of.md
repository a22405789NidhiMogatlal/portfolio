
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
- url

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
- classificação por linguagem favorita


### Competencia
- nome
- categoria

### Categoria
- nome

### Formação
- titulo
- instituição
- data início
- data fim
- certificado

### Projetos Pessoais
- titulo
- descrição
- url github

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


### MakingOf ↔ Outras Entidades (N:1)
- Optei por relacioná-la apenas com `Licenciatura`, `UnidadeCurricular`, `Projeto`, `Competencia` e `TFC`, por serem as entidades mais importantes e com maior necessidade de decisões de modelação.
- As restantes entidades (`Docente`, `Tecnologia` e `Formacao`) não foram incluídas, pois são mais simples e descritivas, não exigindo registo detalhado no MakingOf.

---
 
## 3. Evolução do Modelo
 

 
---
 
## 4. Erros Identificados e Correções
 
### Erro 1
- **Descrição:** ...
- **Correção:** ...
 

---
 
## 5. Apontamentos e Notas
> 
 
---
 
## 6. Uso de IA
- ### Projetos Pessoais vs Projetos de UC 
Inicialmente, considerei separar os projetos em duas entidades distintas: projetos de Unidade Curricular e projetos pessoais. No entanto, após recorrer à IA, foi-me sugerida uma abordagem alternativa, utilizando uma única entidade `Projeto` com um atributo `tipo` para distinguir entre projetos de UC e pessoais.

Esta solução revelou-se mais adequada, uma vez que ambos os tipos de projeto partilham praticamente os mesmos atributos. A separação em duas entidades iria introduzir redundância e duplicação de estrutura no modelo.

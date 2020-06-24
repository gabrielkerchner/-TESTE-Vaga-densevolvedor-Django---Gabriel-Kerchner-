O teste consiste em desenvolver um blog utilizando Django 2+. 

Para iniciar o teste voce deve clonar este repositório e iniciar um projeto django

Requisitos:
 - A app blog deve ter dois modelos, Post(slug, title, content, categories, data_criacao, publicacao) e Category(name, slug);
 - O blog deve ter uma tela de listagem de posts paginada (numero ou load more, o que preferir) com search (por titulo, content, categories..) e uma tela de detalhes do post;
 - É mandatório que voce utilize Bootstrap 4 - https://getbootstrap.com/;
 - O blog deve ter uma API com um endpoint publico para listagem das postagens. Pode ser utilizado Django rest framework para essa funcionalidade.

Desejavel (se optar por fazer, adicionar em uma branch desejavel):
 - Gerar um slug unico a partir do titulo utilizando signals;
 - Adicionar a data que o projeto rodou em uma constante no settings e mostrar na tela;
 - Redirecionar a rota "/" para "/admin" sem criar uma view ou ClassBasedView.

A avaliação irá levar em consideração as boas práticas de desenvolvimento (PEP8) e a compreenção e resolução do problema de forma mais simples possivel.

Quando finalizado, voce deve enviar para o e-mail contact@wiserdev.com o repositório no github com o projeto e o titulo '[TESTE] Vaga densevolvedor Django - <seu nome>'.

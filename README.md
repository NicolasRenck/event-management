# Event Management

Uma aplicação web robusta desenvolvida em Django para facilitar a organização, edição e descoberta de eventos. O sistema foca em uma experiência de usuário limpa, utilizando uma interface baseada em "cards" e "ilhas" de edição totalmente responsivas.



## Funcionalidades

Autenticação e Segurança: Proteção de rotas sensíveis utilizando LoginRequiredMixin, garantindo que apenas usuários autenticados gerenciem conteúdos.

Dashboard Interativo: Interface principal com busca dinâmica e filtros para localização rápida de eventos.

UI Responsiva & Polida: Sistema de grid dinâmico com altura de cards padronizada e tratamento de overflow de texto, garantindo uma interface consistente independente do volume de dados.

Segurança e Permissões: Implementação de LoginRequiredMixin e verificações a nível de View para garantir que usuários só gerenciem seus próprios eventos, além de proteção contra ataques CSRF em todos os formulários.

Persistência de Dados Robusta: Integração total com PostgreSQL, garantindo a integridade dos dados, suporte a transações complexas e prontidão para escalabilidade em ambiente de produção.



## Tecnologias

Backend: Python 3 + Django Framework (Class-Based Views).

Frontend: HTML5, CSS3 (Flexbox/Grid) e integração com o motor de templates do Django.

Banco de Dados: PostgreSQL (Produção).

Controle de Versão: Git e GitHub.



## Screenshots
 

![Home](screenshots/home.png)

![Criar evento](screenshots/addevent.png)

![Página/Detalhes do evento](screenshots/detail.png)

![Página de compra de Tickets](screenshots/tickets.png)



## Como rodar localmente


```bash
git clone https://github.com/NicolasRenck/event-management
cd event_management
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```



**requirements.txt:**
```
asgiref==3.11.1
Django==6.0.4
pillow==12.2.0
psycopg2-binary==2.9.11
python-decouple==3.8
sqlparse==0.5.5
tzdata==2026.1

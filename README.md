# Event Management

Uma aplicação web robusta desenvolvida em Django para facilitar a organização, edição e descoberta de eventos. O sistema foca em uma experiência de usuário limpa, utilizando uma interface baseada em "cards" e "ilhas" de edição totalmente responsivas.

---

## Funcionalidades

- **Autenticação e Segurança:** Proteção de rotas sensíveis utilizando `LoginRequiredMixin`, garantindo que apenas usuários autenticados gerenciem conteúdos.
- **Dashboard Interativo:** Interface principal com busca dinâmica e filtros para localização rápida de eventos.
- **UI Responsiva & Polida:** Sistema de grid dinâmico com altura de cards padronizada e tratamento de overflow de texto, garantindo uma interface consistente independente do volume de dados.
- **Segurança e Permissões:** Verificações a nível de View garantindo que usuários só gerenciem seus próprios eventos, além de proteção contra ataques CSRF em todos os formulários.
- **Upload de Imagens:** Suporte a imagens de capa para eventos via Pillow.
- **Persistência de Dados Robusta:** Integração total com PostgreSQL, garantindo integridade dos dados e prontidão para escalabilidade em ambiente de produção.

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3 + Django (Class-Based Views) |
| Frontend | HTML5, CSS3 (Flexbox/Grid) + Django Templates |
| Banco de Dados | PostgreSQL |
| Containerização | Docker + Docker Compose |
| Upload de Imagens | Pillow |
| Variáveis de Ambiente | Python-Decouple |
| Controle de Versão | Git + GitHub |

---

## Screenshots

![Landing Page](screenshots/landing.png)

![Home](screenshots/home.png)

![Criar evento](screenshots/addevent.png)

![Página/Detalhes do evento](screenshots/detail.png)

![Página de compra de Tickets](screenshots/tickets.png)

---

## Como rodar localmente

### Com Docker (recomendado)

```bash
git clone https://github.com/NicolasRenck/event-management
cd event-management
cp .env.example .env  # preencha as variáveis conforme a seção abaixo
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Acesse: [http://localhost:8000](http://localhost:8000)

---

### Sem Docker

```bash
git clone https://github.com/NicolasRenck/event-management
cd event-management
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=sua_secret_key_aqui
DEBUG=True

DB_NAME=eventdb
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
DB_HOST=db
DB_PORT=5432
```

> **Atenção:** nunca suba o arquivo `.env` real para o repositório. O arquivo `.env.example` serve apenas como referência.
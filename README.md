# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o reposotório.
2. Crie um virtualenv com Python 3.5
3. Ative o vitualenv.
4. Instale as dependências.
5. Configure as intância com o .env
6. Execute os testes.

```console
git clone git@github.com:jlira/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configura o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrig/secret_gen.py`
heroku config:set DEBUG=False
# configurar o email
git push heroku master --force
```


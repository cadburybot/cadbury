# CadburyBot :rocket:

## Sneak Peak 👀

![alt text](https://github.com/cadburybot/cadbury/blob/main/images/cadbury_status.png?raw=true)

## Under development 🚧

Cadbury is a super light-weight APIClient which manages multiple environments like dev/qa/local/prod and you name it.
Unlike cURL which is a command with options based, Cadbury only needs a name to hit request. Cadbury manages all the
requests grouped as environments for you.

And yeah it is a CLI. You don't have to leave your terminal at all. You can just send a request as easy
as `cadbury hit user_login`, where `user_login` is the name for the request that Cadbury manages.

Configuring environments is also so easy. You can use `cadbury env create <env-name>` command and Cadbury creates an
environment for you.

## Installation

Install using pip

```bash
pip install cadburybot
```

Or install it with poetry using:

```bash
poetry add cadburybot
```
    
## Usage
    
Let us assume that you want to create an environment named `dev` and create a user login request named `user_login`.
    

```bash
cadbury env create dev # Cadbury interactively guides you through the creation process. 
cadbury env get dev
cadbury env get # Get all environments.py
cadbury env edit dev
cadbury env delete dev
cadbury env change prod # Changes your current environment

# All requests operations will be done for the current environment
cadbury request create user_login 
cadbury request get user_login 
cadbury request get 
cadbury request edit user_login 
cadbury request delete user_login

cb hit user_login
```

> Pro tip: CadburyBot saves all these configurations as JSON file under `~/cadburybot` directory. Instead of using `request` or `env` command, You can also manually update them.
    
Under the hood, Cadbury manages environments as JSON file. A sample environments.json file with `dev` and `prod` looks like this
    
**~/cadburybot/environments.json**
    
   ```yaml
        {
          "dev": {
            "requests": {
              "user_login": {
                "endpoint": "/api/login",
                "method": "POST",
                "headers": {
                  "Content-Type": "application/json"
                },
                "body": {
                  "username": "msharran-dev",
                  "password": "mysecretpassword"
                }
              }
            },
            "base_url": "https://dev.example.com",
            "token_key": "Authorization",
            "token_value": "Bearer <token>"
          },
          "prod": {
            "requests": {
              "user_login": {
                "endpoint": "/api/login",
                "method": "POST",
                "headers": {
                  "Content-Type": "application/json"
                },
                "body": {
                  "username": "msharran",
                  "password": "mysecretpassword"
                }
              }
            },
            "base_url": "https://example.com",
            "token_key": "Authorization",
            "token_value": "Bearer <token>"
          }
        }
   ```

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the cadburybot project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/cadburybot/cadbury/blob/master/CODE_OF_CONDUCT.md).

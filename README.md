![alt text](https://github.com/cadburybot/cli/blob/main/logo.png?raw=true)
# CadburyBot :rocket:

## Under development 🚧

Cadbury is a super light-weight APIClient which manages multiple environments like dev/qa/local/prod and you name it. Unlike cURL which is a command with options based, Cadbury only needs a name to hit request. Cadbury manages all the requests grouped as environments for you. 
    
And yeah it is a CLI. You don't have to leave your terminal at all. You can just send a request as easy as `cb hit user_login`, where `user_login` is the name for the request that Cadbury manages.

Configuring environments is also so easy. You can use `cb env set <env-name>` command and Cadbury creates an environment for you.
    
## Installation

Add this line to your application's Gemfile:

```ruby
gem 'cadburybot'
```

And then execute:

```bash
bundle install
```

Or install it yourself as:

```bash
gem install cadburybot
```
    
## Usage
    
Let us assume that you want to create an environment named `dev` and create a user login request named `user_login`.
    

```bash
cb env new dev # Cadbury interactively guides you through the creation process. 
cb env get dev
cb env get # Get all environments.py
cb env edit dev
cb env delete dev

cb request new user_login --env dev    
cb request get user_login --env dev
cb request get --env dev 
cb request edit user_login --env dev
cb request delete user_login --env dev

cb hit user_login --env dev
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

Everyone interacting in the cadburybot project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/cadburybot/cli/blob/master/CODE_OF_CONDUCT.md).

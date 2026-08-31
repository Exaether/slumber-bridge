# Slumber Bridge

"Slumber bridge", a precursor project made to reduce the loss of information during transmission.

Provide simple access to Arknights game data through a REST API frontend.

If you've ever seen what the raw game data looks like, you know how complicated and inconsistent it is.
This API is meant to simplify it as much as possible by only keeping relevant information, and exposing multiple endpoints instead of the giant `character_table.json`.

Note that for now, I make this API so i can use it in my own website, so it only expose the data i need.
But it can still be expanded in the future to make it usable by other sites.

# Credits

Huge thanks to [Ashleney](https://github.com/ashleney), [Kengxxiao](https://github.com/Kengxxiao), and every other Arknights devs who provide the actual data.  
I'm only distributing the data, not extracting it, so this project wouldn't exist without them.  
And of course they don't own the data, and neither do I. All data you can find on this API belongs to Hypergryph Network Technology Co., Ltd.

The API is made with [FastAPI](https://fastapi.tiangolo.com/)

# Developing

How to run the dev server.

## Requirements

- python3
- venv

## setting up

- create a venv
- install fastAPI in the venv: `pip install "fastapi[standard]"`
- set the `DATA_RELOAD_KEY` env variable to whatever password you want for the update endpoint

## Running

`fastapi dev main.py`

The API should now be accessible at [localhost:8000](http://127.0.0.1:8000)

# Deploying

If you want to host your own instance of slumber bridge, a docker container is configured.
You just need to run `docker compose build` to build the image,
then create a .env file with the `DATA_RELOAD_KEY` variable, and you can run the server with `docker compose up`

# Endpoints

| Endpoint                       | Description                             |
| ------------------------------ | --------------------------------------- |
| `/`                            | List of all endpoints                   |
| `/operators`                   | List of operators and their basic infos |
| `/operators/{id}`              | Detailed infos about a given operator   |
| `/skills`                      | List of all skills                      |
| `/skills/{id}`                 | Details of a given skill                |
| `/skills/{id}/{level}`         | Details of a given skill level          |
| `/modules`                     | List of all modules                     |
| `/modules/{id}`                | Details of a given module               |
| `/modules/{id}/{level}`        | Details of a given module level         |
| `/ranges`                      | Data about the ranges                   |
| `/ranges/{id}`                 | Data of a given range                   |
| `/subProfNames`                | Sub classes id-to-name dict             |
| `/subProfNames/{id}`           | Name of a given sub-class               |
| `/records`                     | List of all operators records           |
| `/records/{id}`                | An operator record                      |
| `/stories`                     | list of all stories                     |
| `/stories/{id}`                | Detail of a story, and all its stages   |
| `/stories/{id}/index`          | a stage of a story                      |
| `/stories/{id}/index/stripped` | simpler version of a stage              |

## Operators

All endpoints here are under `/operators/{id}`

| Endpoint                         | Description                                                 |
| -------------------------------- | ----------------------------------------------------------- |
| `/trait`                         | Trait of the operator                                       |
| `/trait/{phase}`                 | Trait of the operator at a given elite level                |
| `/talent/{number}`               | Talent of the operator                                      |
| `/talent/{number}/{phase}/{pot}` | Talent of the operator at a given elite level and potential |
| `/potential/{rank}`              | bonus given by a given potential rank                       |
| `/phases/{number}`               | Infos about the given elite level                           |
| `/phases/{number}/stats/{level}` | Stats of the operator at any given level                    |
| `/favor`                         | The trust bonus of the operator                             |
| `/skills/{number}`               | Infos about the given skill                                 |
| `/skills/{number}/{level}`       | Infos about a given level of a skill                        |
| `/skins`                         | List of the operator's skins*                               |
| `/full`                          | All of the above at the same time (except skills)           |

*Note that the elite 0 avatar id is just the op id.

## Maintenance

There's two endpoints to reload the data:

- `/reload`: reload the data from disk, only useful if you do external changes on the data files during runtime.
- `/update`: Fetch data from a source repository ([ArknightsGamedata](https://github.com/ArknightsAssets/ArknightsGamedata/tree/master), can be configured in `core/parser.py`) parse it into the `data` folder, and load it in the server.

Both endpoints require authentification through an API key (the one you defined in [Setting up](#setting-up)) to use them, use:  
`curl -X POST "http://127.0.0.1:8001/update" -H "API-Key: <your key>"`
or anything that can write `"API-Key: <your key>"` in the request header, like the RESTED browser extension.

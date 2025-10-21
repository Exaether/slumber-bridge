# Slumber Bridge

Provide simple access to Arknights game data through a REST API frontend.

If you've ever seen what the raw game data looks like, you know how complicated it is.
This API is meant to simplify it as much as possible by only keeping relevant information, and exposing multiple endpoints instead of the giant `character_table.json`.

Note that for now, I make this API so i can use it in my own website, so it only expose the data i need.
But it can still be expanded in the future to make it usable by other sites.

# Credits
Huge thanks to [Kengxxiao](https://github.com/Kengxxiao), [Yuanyan](https://github.com/yuanyan3060), [PuppiizSunniiz](https://github.com/PuppiizSunniiz), [fexli](https://github.com/fexli) and every other Arknights devs who provide the actual data.
I'm only distributing the data, not extracting it, so this project wouldn't exist without them.
And of course they don't own the data, and neither do I. All data you can find on this API belongs to Hypergryph Network Technology Co., Ltd.

The API is made with [FastAPI](https://fastapi.tiangolo.com/)

# Installation
How to host the api yourself

## requirements
- docker-compose (and docker)
- that's it

## Setting up
- create a `.env` file with the following content:
```
DATA_RELOAD_KEY=<whatever you want>
```
This will be the key you'll need to use when updating the data.
- run `docker-compose build`
- that's it

## Running
`docker-compose up dev` for the dev server, with live reload on file change  
`docker-compose up prod` for the prod server, no live reload  

The API should now be accessible at [localhost:8000](http://127.0.0.1:8000) (on port [8001](http://127.0.0.1:8001) for the dev server)

# Endpoints

|Endpoint|Description|
|--------|-----------|
|`/`|List of all endpoints|
|`/operators`|List of operators and their basic infos|
|`/operators/{id}`|Detailed infos about a given operator|
|`/skills`|List of all skills|
|`/skills/{id}`|Details of a given skill|
|`/skills/{id}/{level}`|Details of a given skill level|
|`/modules`|List of all modules|
|`/modules/{id}`|Details of a given module|
|`/modules/{id}/{level}`|Details of a given module level|
|`/ranges`|Data about the ranges|
|`/ranges/{id}`|Data of a given range|
|`/subProfNames`|Sub classes id-to-name dict|
|`/subProfNames/{id}`|Name of a given sub-class|

## Operators
All endpoints here are under `/operators/{id}`

|Endpoint|Description|
|--------|-----------|
|`/trait`|Trait of the operator|
|`/trait/{phase}`|Trait of the operator at a given elite level|
|`/talent/{number}`|Talent of the operator|
|`/talent/{number}/{phase}/{pot}`|Talent of the operator at a given elite level and potential|
|`/potential/{rank}`|bonus given by a given potential rank|
|`/phases/{number}`|Infos about the given elite level|
|`/phases/{number}/stats/{level}`|Stats of the operator at any given level|
|`/favor`|The trust bonus of the operator|
|`/skills/{number}`|Infos about the given skill|
|`/skills/{number}/{level}`|Infos about a given level of a skill|
|`/skins`|List of the operator's skins*|
|`/full`|All of the above at the same time (except skills)|

*Note that the elite 0 avatar id is just the op id.

## Maintenance

There's two endpoints to reload the data:
- `/reload`: reload the data from disk.
- `/update`: Fetch data from a source repository ([ArknightsGamedata](https://github.com/ArknightsAssets/ArknightsGamedata/tree/master), can be configured in `core/parser.py`) parse it into the `data` folder, and load it in the server.

Both endpoints require authentification through an API key (the one you defined in [Setting up](#setting-up)) to use them, use:  
`curl -X POST "http://127.0.0.1:8001/update" -H "API-Key: <your key>"`
or anything that can write `"API-Key: <your key>"` in the request header

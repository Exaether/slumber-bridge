# Arknights HR Office

Provide simple access to Arknights game data through a REST API frontend.

If you've ever seen what the raw game data looks like, you know how complicated it is.
This API is meant to simplify it as much as possible by only keeping relevant information, and exposing multiple endpoints instead of the giant `character_table.json`.

I am only processing and distributing the data, I'm not extracting it in any way.
Huge thanks to [Kengxxiao](https://github.com/Kengxxiao), [Yuanyan](https://github.com/yuanyan3060), [PuppiizSunniiz](https://github.com/PuppiizSunniiz) and every other arknights devs who provide the actual data.

Note that for now, I make this API so i can use it in my own website, so it only expose the data i need.
But it can still be explanded in the future to make it usable by other sites.

The API is made with [FastAPI](https://fastapi.tiangolo.com/)


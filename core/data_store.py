import json
from pathlib import Path


class DataStore:
    def __init__(self, data_dir: str):
        self.data_dir = Path(__file__).parent.parent / "data"
        self._operators = {}
        self._skills = {}
        self._modules = {}
        self._tokens = {}
        self._ranges = {}
        self._subProfNames = {}

    def load_all(self):
        for file in (self.data_dir / "operators").glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                self._operators[file.stem] = json.load(f)
        for file in (self.data_dir / "skills").glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                self._skills[file.stem] = json.load(f)
        for file in (self.data_dir / "modules").glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                self._modules[file.stem] = json.load(f)
        for file in (self.data_dir / "tokens").glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                self._tokens[file.stem] = json.load(f)
        with open(self.data_dir / "ranges.json") as f:
            self._ranges = json.load(f)
        with open(self.data_dir / "subProfNames.json") as f:
            self._subProfNames = json.load(f)

    def getOperators(self):
        return self._operators

    def getOperator(self, name: str):
        return self._operators[name]

    def getSkills(self):
        return self._skills

    def getSkill(self, name: str):
        return self._skills[name]

    def getModules(self):
        return self._modules

    def getModule(self, name: str):
        return self._modules[name]

    def getTokens(self):
        return self._tokens

    def getToken(self, name: str):
        return self._tokens[name]

    def getRanges(self):
        return self._ranges

    def getRange(self, id: str):
        return self._ranges[id]

    def getSubProfName(self, id: str):
        return self._subProfNames[id]

    def getSubProfNames(self):
        return self._subProfNames


data_store = DataStore("data")

import os


class Pessoa:
    def __init__(self):
        self.nome = "nome"
        self.idade = "idade"


class ReturnEnv():
    def __init__(self, name_env):
        self.name_env = name_env

    def load(self):
        return os.environ[self.name_env]


env = ReturnEnv("KEY_TESTE").load()

print(env)

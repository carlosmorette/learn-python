class Config:
    database_url:str

    def load(self, env_kv_store, config_kv_store):
        database_url = env_kv_store["DATABASE_URL"]

config = Config()

config.load(os.environ, asd )
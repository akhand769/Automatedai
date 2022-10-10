OPENAI_API_KEY = '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'
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}


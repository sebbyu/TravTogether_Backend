
def __set__(setting):
  local_settings = 'backend.settings.local'
  production_settings = 'backend.settings.production'
  local_host = "127.0.0.1"
  production_host = "travtogether.herokuapp.com"
  if setting == "local":
    return local_settings, local_host
  elif setting == "production":
    return production_settings, production_host


CURRENT_SETTING, CURRENT_HOST = __set__("production")
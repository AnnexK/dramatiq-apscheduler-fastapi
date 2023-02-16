from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["./config/settings.yml"],
    environments=False,
)

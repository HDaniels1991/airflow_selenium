
from airflow.plugins_manager import AirflowPlugin
from selenium_plugin.hooks.selenium_hook \
    import SeleniumHook


class SeleniumPlugin(AirflowPlugin):
    name = 'selenium_plugin'
    operators = []
    hooks = [SeleniumHook]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []

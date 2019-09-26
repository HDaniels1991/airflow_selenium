from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from selenium_plugin.hooks.selenium_hook import SeleniumHook
from datetime import datetime


class SeleniumOperator(BaseOperator):
    '''
    Selenium Operator
    '''
    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        #  yesterday = context.get('yesterday_ds')
        hook = SeleniumHook()
        hook.create_container()
        hook.create_driver()

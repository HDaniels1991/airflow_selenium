from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from selenium_plugin.hooks.selenium_hook import SeleniumHook


class SeleniumOperator(BaseOperator):
    '''
    Selenium Operator
    '''
    template_fields = ['script_args']

    @apply_defaults
    def __init__(self,
                 script,
                 script_args,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.script = script
        self.script_args = script_args

    def execute(self, context):
        hook = SeleniumHook()
        hook.create_container()
        hook.create_driver()
        hook.run_script(self.script, self.script_args)
        hook.remove_container()

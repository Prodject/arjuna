from commons import *
from arjuna.tpi.guiauto.helpers import With

init_arjuna()

automator = launch_automator()
go_to_wp_home(automator)

'''
The following code is for user name field.
Html of user name: <input type="text" name="log" id="user_login" class="input" value="" size="20">

Params: 
APP URL: E.g. http://192.168.56.103
Page: E.g. wp-login
Resulting in http://192.168.56.103/wp-login.php
'''

identifier = r"//*[@action='$app_url$/$page$.php']"

app_url = automator.config.get_user_option_value("wp.app.url").as_str()
page = "wp-login"

element = automator.element(With.xpath(identifier).format(app_url=app_url, page=page))
element.identify()
print(element.source.content.root)


# Named params need not be passed in order, providing you flexibility, readability and preventing positional errors.
element = automator.element(With.xpath(identifier).format(page=page, app_url=app_url))
element.identify()
print(element.source.content.root)

# Names for parameters are case-insensitive
element = automator.element(With.xpath(identifier).format(PaGe=page, aPP_Url=app_url))
element.identify()
print(element.source.content.root)

logout(automator)
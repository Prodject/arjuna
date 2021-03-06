from arjuna.tpi.enums import ArjunaOption
from arjuna.client.core.action import *
from arjuna.interact.gui.auto.locator.emd import SimpleGuiElementMetaData

from .guiautomator import GuiAutomator
from .handler import Handler

class SingleActionChain(Handler):

    def __init__(self, automator, element=None):
        super().__init__(automator)
        from arjuna.interact.gui.auto.element.frame import DomRoot
        self.__automator = automator
        self.__element = element
        self.__attached_to_element = element is not None

    def is_click_action(self, action):
        return PartialActionType[action["actionType"]] == PartialActionType.CLICK

    def are_args_defined(self, action):
        return "args" in action

    def get_args(self, action):
        return action["args"]

    def contains_target_element(self, action):
        return "targetElement" in self.get_args(action)

    def get_target_element(self, action):
        return action["args"]["targetElement"]

    def contains_target_point(self, action):
        return "targetPoint" in self.get_args(action)

    def get_target_point(self, action):
        return action["args"]["targetPoint"]

    def perform(self, single_action_chain):
        processed_list = []
        current_action_list = []
        for action in single_action_chain:
            if self.is_click_action(action):
                if not self.are_args_defined():
                    current_action_list.append(("click", dict()))
                    continue

                target_element = None
                if self.contains_target_element(action):
                    target_element_id = self.get_target_element(action)
                    target_element = self.__automator.get_element_for_setu_id(target_element_id)
                elif self.contains_target_point(action):
                    emd = SimpleGuiElementMetaData("point", self.get_target_point(action))
                    element = self.__automator.create_element(emd)
                
                if target_element:
                    target_element.find_if_not_found()
                    current_action_list.append(("click", {"on_element" : (target_element.setu_id, True)}))
                    
        processed_list.append(current_action_list)
        for single_chain in processed_list:
            self.__automator.dispatcher.perform_action_chain(single_chain)


        




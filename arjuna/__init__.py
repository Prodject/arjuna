'''
This file is a part of Test Mile Arjuna
Copyright 2018 Rahul Verma

Website: www.RahulVerma.net

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import pkg_resources
import time
import os
import sys

def join_paths(*paths):
    return os.path.abspath(os.path.join(*paths))

root_dir = join_paths(os.path.dirname(os.path.realpath(__file__)), "..")
importables_dir = join_paths(root_dir, "third_party")

sys.path.insert(0, importables_dir)
sys.path.insert(0, root_dir)

class __arfacade():

    def __init__(self):
        self.__version = pkg_resources.require("arjuna")[0].version

    def launch(self, raw_args):
        from arjuna.core.reader.textfile import TextResourceReader
        from arjuna.interface.cli import ArjunaCLI
        reader = TextResourceReader("header.txt")
        print(reader.read().format(version=self.__version))
        reader.close()

        print("Parsing CLI Options...")
        cli = ArjunaCLI(raw_args)
        # Initialize the Arjuna Core as per CLI options
        print("Intializing Arjuna...")
        cli.init()

        print("Executing Arjuna Command...")
        cli.execute()

Arjuna = __arfacade()

# from arjuna.unitee.markup import tsmarkup

# markup = tsmarkup
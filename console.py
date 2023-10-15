#!/usr/bin/python3
"""
Airbnb Console
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State
import re
import shlex

class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a given class, saves it
        (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg]()
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = storage.all()
        print(all_objs.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = storage.all()
        obj = all_objs.get(key)
        if obj is not None:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        based or not on the class name
        """
        all_objs = storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
        elif arg in HBNBCommand.classes:
            print([str(obj) for obj in all_objs.values()
                   if type(obj).__name__ == arg])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file)
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = storage.all()
        obj = all_objs.get(key)
        if obj is None:
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            setattr(obj, args[2], args[3])
            storage.save()

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            all_objs = storage.all()
            count = sum(1 for obj in all_objs.values()
                        if type(obj).__name__ == arg)
            print(count)

    def default(self, line):
        """
        Default behavior for unknown commands
        """
        full_match = re.fullmatch(r'^(\w+)\.(\w+)(\s+(\(.+\)))?$', line)
        if full_match:
            class_name = full_match.group(1)
            method = full_match.group(2)
            args = full_match.group(4)
            if class_name in HBNBCommand.classes and \
                    hasattr(HBNBCommand.classes[class_name], method):
                eval(f'self.do_{method}("{class_name} {args}")')
                return
        print(f"*** Unknown syntax: {line}")

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit at End of File (EOF)
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" console for testing"""
import cmd
import models
from models import storage
from models.child_milestones import ChildMilestones
from models.base_model import BaseModel
import shlex  # for splitting the line along spaces except in double quotes


classes = {"ChildMilestones": ChildMilestones, "BaseModel": BaseModel}


class SLPCommand(cmd.Cmd):
    """ SLP console """
    prompt = '(SLP) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        '''creates a new instance of a class'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_dict = self._key_value_parser(args[1:])
        new_instance = classes[args[0]](**new_dict)
        new_instance.save()

    def do_show(self, arg):
        '''prints the string representation of an instance'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = args[0] + '.' + args[1]
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")



if __name__ == '__main__':
    SLPCommand().cmdloop()

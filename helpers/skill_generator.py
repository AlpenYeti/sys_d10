#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Not actually part of the project; just easier to maintain everything here
import importlib
import re
import sys,os
import traceback

try:
    # path=os.path.join(os.path.dirname(__file__),"..","minitest")
    # minitest=importlib.import_module("...minitest.minitest","skill_generator")
    from minitest import minitest
    term = minitest.Terminal()
    from test import testReroll,testInit,testWrapper,testParser

except ImportError as e:
    print(e)
    print("Minitest isn't imported, the system cannot execute test units")


try:
    args = sys.argv[1:]
    command = sys.argv[1]
except:
    print("No command specified, just outputting the help")
    command = "help"

EOL = "\n"
tab = "   "
# Custom parsing
ENCAISSEMENT_PARSE = """d_vars.encaissement=to_number(tab[i+1]);
d_vars.encaissement_dices="d20";
if (tab[i+2]=="4") d_vars.encaissement_dices="d10";
i+=3;
break;"""

FLAT_DICES_PARSE = """d_vars.flat_dices[d_vars.nb_flat_dices]=to_p_number(tab[i+1]);
d_vars.nb_flat_dices++;
i+=2;
break;"""

TECHNIQUE_PARSE = """d_vars.technique_m=to_p_number(tab[i+2]);
i+=3;
break;"""
## Custom adders:
lambda_flat_dices = lambda a: "@flat_dices[@flat_dices]=type({tab+1});\n@nb_flat_dices++;"

## Custom rerolls:

categories = ['varname', 'Pretty name', 'nb_args', 'type', 'code', 'id', 'default', 'action', 'parser']
hashedCategories = {}
for c in range(len(categories)):
    hashedCategories[categories[c]] = c


def findCat(element, category):
    return element[hashedCategories[category]]


list = []
# list.append(['varname','Pretty name','nb_args','type','code','id','default','action','parser'])
list.append(['perfection', 'Perfection', 1, 'pint', 'P', 0, 0, "", None])
list.append(['defense_i_0', 'Defence impénétrable simple', 2, 'pint', 'I', 1, 0, "", None])
list.append(['defense_i_1', 'Defence impénétrable expert', 2, 'pint', 'I', 2, 0, "", None])
list.append(['defense_i_2', 'Defence impénétrable meta', 2, 'pint', 'I', 4, 0, "", None])
list.append(['rempart_p', 'Rempart parfait', 1, 'pint', 'R', 0, 0, "", None])
list.append(['technique_m', 'Perfection', 1, 'pint', 'M', 0, 0, "", TECHNIQUE_PARSE])  # +=3
list.append(['coup_d', 'Coup_déchirant', 1, 'pint', 'D', 0, 0, "", None])
list.append(['fauchage', 'Fauchage', 1, 'pint', 'F', 0, 0, "", None])
list.append(['exploiter_p_0', 'Exploiter_les_points_faibles simple', 2, 'pint', 'E', 1, 0, "", None])
list.append(['exploiter_p_1', 'Exploiter_les_points_faibles expert', 2, 'pint', 'E', 2, 0, "", None])
list.append(['exploiter_p_2', 'Exploiter_les_points_faibles meta', 2, 'pint', 'E', 4, 0, "", None])
list.append(['tir_p_0', 'Tir_précis expert', 2, 'pint', 'T', 2, 0, "", None])
list.append(['tir_p_1', 'Tir_précis meta', 2, 'pint', 'T', 4, 0, "", None])
list.append(['tir_i', 'Tir_implacable', 1, 'pint', 'i', 0, 0, "", None])
list.append(['charge', 'Charge', 1, 'pint', 'C', 0, 0, "", None])
list.append(['charge_i', 'Charge_indomptable', 1, 'pint', 'N', 0, 0, "", None])
list.append(['nb_2add', 'Nombre à ajouter', 1, 'int', '+', 0, 0, "+", None])
list.append(['nb_2sub', 'Nombre a soustraire', 1, 'int', '-', 0, 0, "+", None])
list.append(['relances', 'Relances', 1, 'pint', 'r', 0, 0, "", None])
list.append(['seuil', 'Seuil', 1, 'pint', 's', 0, 0, "", None])
list.append(['action', 'Type d\'Action', 1, 'str', 'a', 0, '""', "", None])
list.append(['flat_dices', 'Des fixes', 1, 'pint', 'd', 0, "[]", "+", FLAT_DICES_PARSE])
list.append(['on_hit_c', 'Dégats a l\'impact critique', 1, 'int', 'H', 0, 0, "+", None])
list.append(['attribute', 'Caractéristique', 1, 'int', 'A', 0, 0, "+", None])
list.append(['encaissement', 'Encaissement', 1, 'pint', 'S', 0, 0, "",
             ENCAISSEMENT_PARSE])  # It's actually 2 args but no switch
list.append(['replace', 'Des de substitution', 1, 'int', 'L', 0, -1, "", None])
list.append(['add_to_all', 'Valeur d\'ajout aux des', 1, 'int', 'l', 0, 0, "", None])
list.append(['max_dices', 'Nombre de des max', 1, 'pint', 'm', 0, -1, "", None])
list.append(['player_name', 'Nom du joueur', 1, 'str', 'n', 0, '""', "", None])

list.append(['crit_level', 'Niveau de critique', 1, 'pint', 'c', 0, 2, "", None])
list.append(['transcendence', 'Transcendence', 1, 'pint', 't', 0, 3, "", None])
list.append(['pctreceived', 'Pourcentage dégats recus', 1, 'int', 'v', 0, 0, "", None])
list.append(['pctinflicted', 'Pourcentage dégats infligés', 1, 'int', 'f', 0, 0, "", None])

list.append(['nb_dices', 'Nombre de des', 1, 'pint', '', 0, 0, "", None])
list.append(['nb_flat_dices', 'Nombre de des fixes', 1, 'pint', '', 0, 0, "", None])
list.append(['encaissement_dices', 'Perfection', 1, 'pint', '', 0, '""', "", None])
list.append(['results', 'Resultats', 1, 'pint', '', 0, "[]", "", None])
list.append(['cleave', 'Fauchage', 1, 'pint', '', 0, "[]", "", None])
list.append(['encaissement_result', 'Resultat d\'encaissement', 1, 'pint', '', 0, 0, "", None])
list.append(['technique_result', 'Dégats technique martiale', 1, 'int', '', 0, 0, "", None])
list.append(['coup_d_results', 'Coup déchirant results', 1, 'pint', '', 0, "[]", "", None])


class megaListWrapper():
    def __init__(self, table=list):
        self.table = table
        self.len = len(table)
        self.indexes = {}
        for i in range(len(table)):
            self.indexes[findCat(table[i], "varname")] = i
        # Theese are array because you can't acess them directly
        self.singles = []
        self.code = []
        self.doubles = {}
        for i in table:
            if findCat(i, 'nb_args') == 1:
                self.singles.append(i)
            elif findCat(i, 'nb_args') == 2:
                n = findCat(i, 'code')
                if n not in self.doubles:
                    self.doubles[n] = []
                self.doubles[n].append(i)
            if findCat(i, 'code') != '':
                self.code.append(i)

    def __getitem__(self, argument):  # Actually return the full line as a list wrapper
        return listWrapper(self.table[self.indexes[argument]])

    def __iter__(self):
        for index, key in self.indexes.items():
            yield self[index]

    def itersingles(self):
        "Only iterate over the simple argument ones"
        for index in self.singles:
            yield self[findCat(index, 'varname')]

    def iterdoubles(self):
        "Only iterate over the double arguments ones return a table with all"
        for table in self.doubles.values():
            yield [self[findCat(l, 'varname')] for l in table]

    def iterdefined(self):
        "Only iterate over the ones with defined code"
        pass

    def __contains__(self, val):
        return val in self.indexes

    def __len__(self):
        return self.len

    def pprint(self):
        for e in self:
            print(e[0], ":", e)


class listWrapper():
    def __init__(self, list, index=hashedCategories):
        self.list = list
        self.indexes = index

    def pprint(self):
        print(self.list)

    def asList(self):
        return self.list

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return str(self.list)

    def __getitem__(self, nb):
        return self.list[nb]

    def __getattr__(self, index):
        return self.list[self.indexes[index]]

    def __iter__(self):
        for e in self.list:
            yield e


## Commands
def initialise(args):
    "Initialise the variables for the switch"
    text = "var d_vars={"
    for line in list:
        text += '"{}":{},'.format(line[0], line[6])
    text = text[:-1] + '};'
    return text


def pprint(args):
    "Print the whole list of values"
    for i in list:
        print(i)


def pErrors(name, errors):
    "Print success or error of given test"
    if errors:
        print("{:<15}: {} errors occured".format(name, errors))
    else:
        print("{:<15}: All test successful".format(name))
    return errors


def reroll(args):
    "Generate the reroll inline message"

    reroll = "var msg_relance=\"<a class='sheet-rolltemplate-d10fight' href='!crit 0"

    def addZero(name):
        return '"+d_vars.{}+"'.format(name)

    def addOne(code, name):
        return ' {} {}'.format(code, addZero(name))

    def addTwo(code, id, name):
        return ' {} {} {}'.format(code, id, addZero(name))

    def addSimple(wline):
        if wline.code != "" and wline.code not in ("r", "+", 'M', 'D', "d", "S"):
            if wline.nb_args == 1:
                return addOne(wline.code, wline.varname)
            elif wline.nb_args == 2:
                return addTwo(wline.code, wline.id, wline.varname)
        else:
            # print("{} must be handled differently".format(wline.varname))
            return ""

    # Actual adding of all the lines
    for l in wrapper:
        reroll += addSimple(l)

    # Some lines needs to be added afterwards
    reroll += ' + "+(d_vars.{}+d_vars.{}+d_vars.{})'.format(wrapper["nb_2add"].varname,
                                                            wrapper["technique_result"].varname,
                                                            wrapper["encaissement_result"].varname)

    # Last part of the command
    reroll += '+" r ?{Relances ?}";\n'
    reroll += 'for (var i=0,len=d_vars.results.length;i<len;i++) msg_relance+=" d "+d_vars.results[i];\n'
    reroll += 'msg_relance+="\'>Relancer ce jet</a>";'

    return reroll


def find_code(args):
    "Find the next available code for given name"
    try:
        code = args[1]
    except:
        print("One argument expected")
        return 0
    listFree = ''
    for letter in code:
        Letter = letter.capitalize()
        free, Free = 1, 1
        for line in wrapper:
            if free and letter == line.code:
                free = 0
            if Free and Letter == line.code:
                Free = 0
            if not free and not Free:
                break
        if Free and Letter not in listFree:
            listFree += Letter
        if free and letter not in listFree:
            listFree += letter
    if listFree:
        if len(listFree) == 1:
            return 'The code "{}" is available.'.format(listFree)
        else:
            return 'The following codes "{}" are available'.format(listFree)
    else:
        print('No letter from name "{}" is available'.format(code))
        print(find_code([0, "abcdefghijklmnopqrstuvwxyz&_?.§!;"]))


def parser(args):
    "Generate the argument parser"
    res = tab + "if (len_args>0){" + EOL
    res += tab * 2 + "d_vars.nb_dices=to_p_number(tab[0]);" + EOL
    res += tab + "}" + EOL
    res += tab + "for (i = 1; i < len_args;) {" + EOL
    res += tab * 2 + "switch(tab[i]) {" + EOL

    def typewise(type):
        if type == "pint":
            return "to_p_number({});"
        elif type == 'int':
            return "to_number({});"
        return "{};"

    doubles = {}
    for elt in wrapper.itersingles():
        if elt.parser:
            res += tab * 3 + 'case "{}":'.format(elt.code) + EOL
            for l in elt.parser.splitlines():
                res += tab * 4 + l + EOL
        elif elt.code != "":
            res += tab * 3 + 'case "{}":'.format(elt.code) + EOL
            res += tab * 4 + 'd_vars.{}{}={}'.format(elt.varname, elt.action,
                                                     typewise(elt.type).format("tab[i+1]")) + EOL
            res += tab * 4 + 'i+=2;' + EOL
            res += tab * 4 + 'break;' + EOL
    for grp in wrapper.iterdoubles():
        res += tab * 3 + 'case "{}":'.format(grp[0].code) + EOL
        res += tab * 4 + 'switch (tab[i+1]) {' + EOL
        for elt in grp:
            if elt.parser:
                for l in elt.parser.splitlines():
                    res += tab * 5 + l + EOL
            elif elt.code != "":
                res += tab * 5 + 'case "{}":'.format(elt.id) + EOL
                res += tab * 6 + 'd_vars.{}{}={}'.format(elt.varname, elt.action,
                                                         typewise(elt.type).format("tab[i+2]")) + EOL
                res += tab * 6 + 'break;' + EOL
        if not elt.parser:
            res += tab * 4 + "}" + EOL
            res += tab * 4 + 'i+=3;' + EOL
            res += tab * 4 + 'break;' + EOL

    res += tab * 3 + "default:" + EOL
    res += tab * 4 + 'logit("Argument "+tab[i]+" unknown.");' + EOL
    res += tab * 4 + "i++;" + EOL
    res += tab * 4 + "break;" + EOL
    res += tab * 2 + "}" + EOL
    res += tab * 1 + "}" + EOL
    return res

def export(args):
    if len(args) > 1:
        filen = args[1]
    try:
        f = open(filen)
    except:
        filen = "export.log"
        f = open(filen, "w+")

    def title(t):
        return "{} {} {}".format("#" * 10, t, "#" * 10) + EOL

    f.write(title("Relances"))
    f.write(reroll([]) + EOL)
    f.write(title("Reroll"))
    f.write(initialise([]) + EOL)
    f.write(title("Parse"))
    f.write(parser([]) + EOL)

    f.close()

    return "All data written in '{}'".format(filen)


def test_all(args):
    "Execute all tests"
    subclass = minitest.testGroup("Main Classes", term, verbose=True)
    all_s, t = ["reroll", "init", "wrapper", "parser"], 0
    if len(args) > 1:
        sub = []  # A list of test to execute
        for a in args[1:]:
            a = a.strip("-")
            if a in all_s or a == "all":
                t += 1
                sub.append(a.strip("-"))
            else:
                print("Argument {} unknown".format(a))
    else:
        sub = all_s
        t = len(sub)

    if "all" in sub or "reroll" in sub:
        # "Check the reroll inline generation"
        subclass.addTest(testReroll())
    if "all" in sub or "init" in sub:
        # "Check the initialisation message"
        subclass.addTest(testInit())
    if "all" in sub or "wrapper" in sub:
        # "Test the wrapper, only useful internally"
        subclass.addTest(testWrapper())
    if "all" in sub or "parser" in sub:
        # "Check the reroll inline generation"
        subclass.addTest(testParser())

    if t > 0:
        subclass.test()
        status = subclass.get_status()
        return status['failure']
    return 0

def help(args):
    "Help, print the following message"
    print("List of availables commands")
    for key in commands.keys():
        print("   {}: {}".format(key, commands[key].__doc__))


commands = {"init": initialise, "print": pprint, "reroll": reroll,
            "test": test_all, "code": find_code, "parser": parser, "export": export, "help": help}

if __name__ == '__main__':
    wrapper = megaListWrapper()
    try:
        ret = commands[command](args)
        if ret:
            print(ret)
    except KeyError:
        print("Command {} doesn't exist".format(command))
        commands['help'](args)
    except Exception:
        print("Couldn't execute command " + command)
        print("  > {} ({})".format(sys.exc_info()[1], sys.exc_info()[0]))
        traceback.print_tb(sys.exc_info()[2])

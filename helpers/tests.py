import minitest
import re
from skill_generator import *

__all__=["testParser","testWrapper","testInit","testReroll"]

class testInit(minitest.simpleTestUnit):
    """Check the initialisation message"""

    def __init__(self):
        super(testInit, self).__init__("initialisation variables")

    def _testInit(self):
        self.currentTest("generating test values")

        test_values = {"nb_dices": 0, "perfection": 0, "defense_i_0": 0, "defense_i_1": 0,
                       "defense_i_2": 0, "rempart_p": 0, "technique_m": 0, "coup_d": 0, "coup_d_results": "[]",
                       "fauchage": 0, "exploiter_p_0": 0, "exploiter_p_1": 0, "exploiter_p_2": 0, "tir_p_0": 0,
                       "tir_p_1": 0, "tir_i": 0, "charge": 0, "charge_i": 0, "nb_2add": 0, "nb_2sub": 0, "relances": 0,
                       "seuil": 0, "nb_flat_dices": 0, "action": '""', "flat_dices": "[]", "results": "[]",
                       "technique_result": 0,
                       "cleave": "[]", "on_hit_c": 0, "attribute": 0, "encaissement": 0, "encaissement_dices": '""',
                       "encaissement_result": 0, "replace": -1, "add_to_all": 0, "max_dices": -1, "player_name": '""'}
        a = len(test_values)
        b = len(list)
        try:
            dict_list = {}
            for l in list:
                dict_list[l[0]] = l[6]
            self.addSuccess()
        except Exception as ex:
            self.addFailure(str(ex))

        self.currentTest("testing list")
        if a < b:
            pass  # Only if the values are updated
        #    self.addFailure("Too many values in the list")
        #    for l in dict_list.keys():
        #        if l not in test_values:
        #            self.currentTest(l)
        #            self.addFailure("{} missing from the test template".format(l))
        elif b < a:
            self.addFailure("Too few values in the list")
            for t, v in test_values.items():
                if t not in dict_list.keys():
                    self.currentTest(t)
                    self.addFailure("Missing element {}".format(v))
        else:
            for l, vl in dict_list.items():
                if l in test_values.keys():
                    if test_values[l] != vl:
                        self.currentTest(test_values[l])
                        self.addFailure("Expected {}, got {}".format(l, vl))
                else:
                    self.currentTest(l)
                    self.addFailure("The element is not in the test values")
            self.addSuccess()


class testReroll(minitest.simpleTestUnit):
    """Check the reroll inline message"""

    def __init__(self):
        super(testReroll, self).__init__("inline message")

    def _testReroll(self):
        self.currentTest("regex generation")
        model = """"var msg_relance="<a class='sheet-rolltemplate-d10fight' href='!crit 0 P "+d_vars.perfection+" I 1 "+d_vars.defense_i_0+" I 2 "+d_vars.defense_i_1+" I 4 "+d_vars.defense_i_2+" R "+d_vars.rempart_p+" F "+d_vars.fauchage+" E 1 "+d_vars.exploiter_p_0+" E 2 "+d_vars.exploiter_p_1+" E 4 "+d_vars.exploiter_p_2+" T 2 "+d_vars.tir_p_0+" T 4 "+d_vars.tir_p_1+" i "+d_vars.tir_i+" C "+d_vars.charge+" N "+d_vars.charge_i+" + "+(d_vars.nb_2add+d_vars.technique_result+d_vars.encaissement_result)+" - "+d_vars.nb_2sub+" r ?{Relances ?}"+" s "+d_vars.seuil+" a "+d_vars.action+" H "+d_vars.on_hit_c+" A "+d_vars.attribute+" L "+d_vars.replace+" l "+d_vars.add_to_all+" m "+d_vars.max_dices+" n "+d_vars.player_name;
        for (var i=0,len=d_vars.results.length;i<len;i++) msg_relance+=" d "+d_vars.results[i];
        msg_relance+="'>Relancer ce jet</a>";"""
        var = re.compile(' ([a-zA-Z:+_] .*?".*?)(?:\+"|;)')
        self.addSuccess()

        self.currentTest('generating inline message')
        roll = reroll(args)
        self.addSuccess()

        self.currentTest("checking generated roll")
        for e in (var.findall(model)):
            if roll.find(e) < 0:
                self.currentTest("[{}]".format(e))
                self.addFailure("missing value")
        self.addSuccess()

        # Only if the args are updated
        # self.currentTest("checking model")
        # for e in var.findall(roll):
        #    if model.find(e)<0:
        #        self.currentTest("[{}]".format(e))
        #        self.addFailure("missing value")
        # self.addSuccess()


class testWrapper(minitest.simpleTestUnit):
    """Check the reroll inline message"""

    def __init__(self):
        super(testWrapper, self).__init__("inline message")

    def _testWrapper(self):
        self.currentTest("generating wrapper")
        s = len(hashedCategories)
        errors=0
        try:
            wrapper[-1]
            errors += 1
            self.addFailure("Error: Element -1 shouldn't exist")
        except:
            self.addSuccess()

        f = 0
        self.currentTest("hashing categories")
        for ele in wrapper:
            for c in hashedCategories.keys():
                if ele.__getattr__(c) != findCat(ele, c):
                    f += 1
                    self.currentTest(ele[0])
                    self.addFailure("{} found, should be {}".format(findCat(ele, c), ele.__getattr__(c)))

            for i in range(s):
                if wrapper[ele[0]][i] != ele.asList()[i] or wrapper[ele[0]][i] != ele[i]:
                    f += 1
                    self.currentTest(i)
                    self.addFailure("Element differs {}!={}".format(wrapper[ele[0]][i], ele.asList()[i]))
        if f == 0:
            self.addSuccess()
        else:
            self.addFailure("{} elements failed".format(f))

        f = 0
        self.currentTest("single variable")
        for i in wrapper.itersingles():
            if i[0] not in wrapper:
                f += 1
                self.addFailure("{} element missing".format(i[0]), nonDestructive=True)
        if f == 0:
            self.addSuccess()
        else:
            self.addFailure("{} elements failed".format(f))

        f = 0
        self.currentTest("double variables")
        for l in wrapper.iterdoubles():
            for i in l:
                if i[0] not in wrapper:
                    f += 1
                    self.addFailure("{} element missing".format(i[0]), nonDestructive=True)
        if f == 0:
            self.addSuccess()
        else:
            self.addFailure("{} elements failed".format(f))


class testParser(minitest.simpleTestUnit):
    """Check the reroll inline message"""

    def __init__(self):
        super(testParser, self).__init__("inline message")

    def _testParser(self):
        self.currentTest("loading parser")
        par = parser(args)
        self.addSuccess()
        f = 0
        nb_code = 0
        self.currentTest("testing all variables")
        for line in list:
            cat = findCat(line, "code")
            if cat != "":
                nb_code += 1
                if 'case "{}"'.format(cat) not in par:
                    f += 1
                    self.addFailure("code {} not found".format(cat), nonDestructive=True)
                if 'd_vars.{}'.format(findCat(line, "varname")) not in par:
                    f += 1
                    self.addFailure("variable {} not found".format(findCat(line, "varname")), nonDestructive=True)
        if f == 0:
            self.addSuccess()
        else:
            self.addFailure("{} failures".format(f))

        self.currentTest("testing i++ count")
        count = par.count("i+=")
        nb_code = nb_code + len([l for l in wrapper.iterdoubles()]) - sum([len(l) for l in wrapper.iterdoubles()])
        if count != nb_code:
            self.addFailure("{} occurences found (expected {})".format(par.count("i+="), nb_code))
        else:
            self.addSuccess()

        self.currentTest("counting {}")
        counto = par.count("{")
        countc = par.count("}")
        tot = len([l for l in wrapper.iterdoubles()]) + 3
        if counto != countc or counto != tot:
            self.addFailure("found {} '{{' and {} '}}   ' instead of {}".format(counto, countc, tot))
        else:
            self.addSuccess()

        f = 0
        self.currentTest("checking special text")
        for line in list:
            cat = findCat(line, "parser")
            if cat:
                for l in cat.splitlines():
                    if l not in par:
                        self.addFailure("{} isn't in the end result".format(l), nonDestructive=True)
        if f == 0:
            self.addSuccess()
        else:
            self.addFailure("{} failures".format(f))
        """for varname with symbol, find symbol
        for Special text, find special
        """

term = minitest.Terminal()
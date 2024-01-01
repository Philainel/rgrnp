#!/usr/bin/env python
import random

#region parsetypes
class Say:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def to_string(self):
        return f"{self.name + ' ' if self.name != '' else self.name}\"{self.expression}\""


class Background:
    def __init__(self, color_or_image):
        self.color_or_image = color_or_image
        
    def to_string(self):
        return f"scene {self.color_or_image}"


class Switch:
    def __init__(self, script):
        self.script = script

    def to_string(self):
        return f"jump {self.script}"
    
class Character:
    def __init__(self, name):
        self.name = name

class PlainText:
    def __init__(self, text):
        self.text = text

    def to_string(self):
        return f"# {self.text}"
#endregion

label = "chapter2_dayfirst_sasha_seems_end"
file = "util/start.md"
output = f"util/{label}.rpy"
switch = "final_message"
start = 1352
end = None
lines = []
expressions = []
write = 1
stdout = 0

with open(file) as F:
    for line in list(map(lambda x: x.rstrip(), F.readlines()[start:end])):
        lines.append(line)

previous = ""

# Statuses:
# 0 - Waiting
# 1 - Bundling Says
#
status = 0

# previousSay = Say("", "")
for line in lines:
    if status == 0:
        if line.startswith("***"):
            expressions.append(Background(line[3:-3]))
        elif line.startswith("~~  "):
            status = 1
            end = -1 if line.endswith("”") else None
            previous = ""
            expressions.append(Say("", line[5:end].replace("\"", "\\\"")))
        elif line.startswith("//"):
            expressions.append(PlainText(line[3:]))
        elif line == "":
            continue
        else:
            status = 1
            previous = line
    elif status == 1:
        if line == "":
            previous = ""
            status = 0
        else:
            start = 6 if line.startswith("    –") else None
            end = (-1 if previous == "" else 0) + (-1 if line.endswith("”") else 0)
            end = end if end != 0 else None
            expressions.append(Say(previous, line[start:end].replace("\"", "\\\"")))
    
if switch != "":
    expressions.append(Switch(switch))

if stdout:
    print("\n".join(list(map(lambda x: x.to_string(), expressions))))
if write:
    with open(output, "w") as F:
        parsed_expressions = [""] #+ list(map(lambda x: x.to_string(), expressions))
        # character_names = set(map(lambda x: x.name, list(filter(lambda x: isinstance(x, Say), expressions))))
        # print(character_names)
        parsed_names = list()
        for e in expressions:
            if isinstance(e, Say):
                if e.name != "":
                    if not e.name in parsed_names:
                        parsed_names.append(e.name)
                    exp = Say(
                            f"char_{label}_{parsed_names.index(e.name)}", 
                            e.expression)
                    parsed_expressions.append(exp.to_string())
                else:
                    parsed_expressions.append(Say("", "~ " + e.expression + " ~").to_string())
            else:
                parsed_expressions.append(e.to_string())
        F.write("# Builded with util/parse.py\n\n" + "\n".join(map(lambda x: f'define char_{label}_{parsed_names.index(x)} = Character("{x}")', parsed_names)) + f"\n\nlabel {label}:" + "\n    ".join(parsed_expressions) + "\n")

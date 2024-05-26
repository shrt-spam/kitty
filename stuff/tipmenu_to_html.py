from string import Template
import re
pattern = r'(.*)\(([0-9]*)\)'

tmpl="""
<li><span>$tip_value TKS</span>$text</li>
"""
tmpl_r="""
<li>$text<span>$tip_value TKS</span></li>
"""
template = Template(tmpl)
template_r = Template(tmpl_r)


# with open("obedient-menu.txt", "r") as f:
#     template = template_r
with open("fun-menu.txt", "r") as f:
    for line in f:
        line = line.strip()
        match = re.search(pattern, line)

        if match:
            result1 = match.group(1)
            tip = match.group(2)
            # print("Result 1:", result1)
            # print("Result 2:", tip)

            s = template.substitute(tip_value=tip, text=result1.strip())
            print(s.strip())
        else:
            print("Pattern not found in the string: " + line)
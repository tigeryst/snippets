invoker_spells = {
    "QQQ": "cold snap",
    "QQW": "ghost walk",
    "QQE": "ice wall",
    "QWW": "tornado",
    "QWE": "deafening blast",
    "QEE": "forge spirit",
    "WWW": "EMP",
    "WWE": "alacrity",
    "WEE": "chaos meteor",
    "EEE": "sun strike"
}

orb_combo = {
    "QQQ": ["qqq"],
    "QQW": ["qqw", "qwq", "wqq"],
    "QQE": ["qqe", "qeq", "eqq"],
    "QWW": ["qww", "wqw", "wwq"],
    "QWE": ["qwe", "qew", "wqe", "weq", "eqw", "ewq"],
    "QEE": ["qee", "eqe", "eeq"],
    "WWW": ["www"],
    "WWE": ["wwe", "wew", "eww"],
    "WEE": ["wee", "ewe", "eew"],
    "EEE": ["eee"]
}

def search_spell(input):
  for key, value in orb_combo.items():
    combination = orb_combo[key]
    print(combination)
    for i in range(len(combination)):
      if combination[i] == input:
        return invoker_spells[key]

  return "Not found"

user_input = input("Enter your orb combo: ")
user_input = list(user_input)
user_input.sort()
" ".join(map(str, user_input))
print(user_input)

print(search_spell(user_input))
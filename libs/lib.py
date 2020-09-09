import all_types

types = [["type", ["target"], lambda n: n.type],
         ["str", ["target"], lambda n: all_types.String(str(n.value))],
         ["int", ["target"], lambda n: all_types.Number(int(n.value))],
         ["float", ["target"], lambda n: all_types.Number(float(n.value))],
         ["bool", ["target"], lambda n: all_types.Boolean(bool(n.value))]]

io = [["print", ["expr", "end"], lambda e, end: print(e, end=end.value)],
      ["input", ["string"], lambda s: input(s)]]

get = {"types": types, "io": io}

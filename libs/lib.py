import all_types

core = [["type", ["target"], lambda n: n.type], ["str", ["target"], lambda n: all_types.String(n)]]

get = {"core": core}

import geg

data = [
    {
        "A": 1,
        "B": 5,
        "C": 4
    },
    {
        "A": 8,
        "B": 16,
        "C": 12
    },
    {
        "A": 123,
        "B": 456,
        "C": 789
    }
]

geg.save_data(data, ["C", "A", "B", "A"],
    "resultado.xlsx", "Hoja 1", "A1")
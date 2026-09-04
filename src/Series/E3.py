def serie(sumatoria: int, inicio: int, fin: int) -> int:
    for n in range(inicio, fin):
        sumatoria = sumatoria + ((-1) ** (n + 1))
        print(f"n[{n}]")
        print(f"(-1) ** ({n + 1}): {(-1)**(n + 1)} \n")

    return sumatoria


sumatoria: int = 0
sumatoria = serie(sumatoria, 1, 5)
print(f"Sumatoria Total : {sumatoria}")

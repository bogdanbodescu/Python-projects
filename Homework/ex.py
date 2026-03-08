import os, csv, json

ROOT = "school_files"

filo = []     # elevi din classA (CSV)
mate = []     # elevi din classB (JSON)

# 1) parcurgere recursivă + citire
for root, dirs, files in os.walk(ROOT):
    for file in files:
        path = os.path.join(root, file)

        # ClassA: CSV (Filologie)
        if "classA" in root and file.endswith(".csv"):
            with open(path, "r", encoding="utf-8-sig") as f:
                r = csv.DictReader(f)
                for row in r:
                    # presupunem coloane: name, class, History, Average
                    row["History"] = float(row["History"])
                    row["Average"] = float(row["Average"])
                    row["_src"] = path
                    filo.append(row)

        # ClassB: JSON (Mate-Info)
        if "classB" in root and file.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)  # listă de elevi
                for st in data:
                    st["average"] = float(st["average"])
                    st["_src"] = path
                    mate.append(st)

# 2) Filologie: Istorie > 90
print("\nFilologie (classA) - Istorie > 90:")
for s in filo:
    if s["History"] > 90:
        print(f'{s["name"]} | {s["class"]} | History={s["History"]}')

# 3) Mate-Info: media < 80
print("\nMate-Info (classB) - media < 80:")
for s in mate:
    if s["average"] < 80:
        print(f'{s["name"]} | {s["class"]} | avg={s["average"]:.2f}')

# 4) Media generală Filologie (toți elevii)
if filo:
    avg_filo = sum(s["Average"] for s in filo) / len(filo)
    print(f"\nMedia generală Filologie: {avg_filo:.2f}")
else:
    print("\nMedia generală Filologie: N/A (fără elevi)")

# 5) Clase Mate-Info ordonate crescător după media clasei
mate_by_class = {}
for s in mate:
    mate_by_class.setdefault(s["class"], []).append(s["average"])

class_avg = []
for c, avgs in mate_by_class.items():
    class_avg.append((c, sum(avgs) / len(avgs)))

class_avg.sort(key=lambda x: x[1])

print("\nMate-Info - clase ordonate după media clasei:")
for c, a in class_avg:
    print(f"{c}: {a:.2f}")

# 6) Cel mai bun elev din fiecare clasă (din ambele profile)
all_students = []
for s in filo:
    all_students.append((s["class"], s["name"], s["Average"]))
for s in mate:
    all_students.append((s["class"], s["name"], s["average"]))

best = {}
for cls, name, avg in all_students:
    if cls not in best or avg > best[cls][1]:
        best[cls] = (name, avg)

print("\nTop elev din fiecare clasă:")
for cls in sorted(best):
    name, avg = best[cls]
    print(f"{cls}: {name} ({avg:.2f})")

# 7) CSV (Filologie) -> JSON
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if "classA" in root and file.endswith(".csv"):
            in_path = os.path.join(root, file)
            out_path = in_path[:-4] + ".json"

            with open(in_path, "r", encoding="utf-8-sig") as f:
                rows = list(csv.DictReader(f))

            with open(out_path, "w", encoding="utf-8") as g:
                json.dump(rows, g, ensure_ascii=False, indent=2)

# 8) JSON (Mate-Info) -> CSV
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if "classB" in root and file.endswith(".json"):
            in_path = os.path.join(root, file)
            out_path = in_path[:-5] + ".csv"

            with open(in_path, "r", encoding="utf-8") as f:
                rows = json.load(f)  # listă de dict

            if not rows:
                continue

            # scriem coloanele după cheile din primul elev
            cols = list(rows[0].keys())

            with open(out_path, "w", encoding="utf-8", newline="") as g:
                w = csv.DictWriter(g, fieldnames=cols)
                w.writeheader()
                w.writerows(rows)

print("\nConversii gata (CSV<->JSON).")
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl

file_path = r"\mnt\Frequencies.xlsx"

df = pd.read_excel(file_path)

# Convert to dictionary: Element -> Difference
values = dict(zip(df["Element"], df["Difference"]))

for k in values:
    if pd.isna(values[k]):
        values[k] = 0.0
# Position of elements in the periodic table
positions = {
    # Period 1
    "H": (0, 0), "He": (0, 17),

    # Period 2
    "Li": (1, 0), "Be": (1, 1),
    "B": (1, 12), "C": (1, 13), "N": (1, 14),
    "O": (1, 15), "F": (1, 16), "Ne": (1, 17),

    # Period 3
    "Na": (2, 0), "Mg": (2, 1),
    "Al": (2, 12), "Si": (2, 13), "P": (2, 14),
    "S": (2, 15), "Cl": (2, 16), "Ar": (2, 17),

    # Period 4
    "K": (3, 0), "Ca": (3, 1),
    "Sc": (3, 2), "Ti": (3, 3), "V": (3, 4), "Cr": (3, 5),
    "Mn": (3, 6), "Fe": (3, 7), "Co": (3, 8), "Ni": (3, 9),
    "Cu": (3, 10), "Zn": (3, 11),
    "Ga": (3, 12), "Ge": (3, 13), "As": (3, 14),
    "Se": (3, 15), "Br": (3, 16), "Kr": (3, 17),

    # Period 5
    "Rb": (4, 0), "Sr": (4, 1),
    "Y": (4, 2), "Zr": (4, 3), "Nb": (4, 4), "Mo": (4, 5),
    "Tc": (4, 6), "Ru": (4, 7), "Rh": (4, 8), "Pd": (4, 9),
    "Ag": (4, 10), "Cd": (4, 11),
    "In": (4, 12), "Sn": (4, 13), "Sb": (4, 14),
    "Te": (4, 15), "I": (4, 16), "Xe": (4, 17),

    # Period 6
    "Cs": (5, 0), "Ba": (5, 1),
    "Hf": (5, 3), "Ta": (5, 4), "W": (5, 5),
    "Re": (5, 6), "Os": (5, 7), "Ir": (5, 8), "Pt": (5, 9),
    "Au": (5, 10), "Hg": (5, 11),
    "Tl": (5, 12), "Pb": (5, 13), "Bi": (5, 14),
    "Po": (5, 15), "At": (5, 16), "Rn": (5, 17),

    # Period 7
    "Fr": (6, 0), "Ra": (6, 1),
    "Rf": (6, 3), "Db": (6, 4), "Sg": (6, 5),
    "Bh": (6, 6), "Hs": (6, 7), "Mt": (6, 8),
    "Ds": (6, 9), "Rg": (6, 10), "Cn": (6, 11),
    "Nh": (6, 12), "Fl": (6, 13), "Mc": (6, 14),
    "Lv": (6, 15), "Ts": (6, 16), "Og": (6, 17),

    # Lanthanides
    "La": (8, 2), "Ce": (8, 3), "Pr": (8, 4), "Nd": (8, 5),
    "Pm": (8, 6), "Sm": (8, 7), "Eu": (8, 8), "Gd": (8, 9),
    "Tb": (8, 10), "Dy": (8, 11), "Ho": (8, 12),
    "Er": (8, 13), "Tm": (8, 14), "Yb": (8, 15), "Lu": (8, 16),

    # Actinides
    "Ac": (9, 2), "Th": (9, 3), "Pa": (9, 4), "U": (9, 5),
    "Np": (9, 6), "Pu": (9, 7), "Am": (9, 8), "Cm": (9, 9),
    "Bk": (9, 10), "Cf": (9, 11), "Es": (9, 12),
    "Fm": (9, 13), "Md": (9, 14), "No": (9, 15), "Lr": (9, 16)
}

fig, ax = plt.subplots(figsize=(20, 13))

cmap = plt.cm.RdBu_r
norm = mpl.colors.TwoSlopeNorm(vmin=-300, vcenter=0, vmax=1700)

for elem, (row, col) in positions.items():
    val = values.get(elem, 0.0)

    ax.add_patch(
        patches.Rectangle(
            (col, -row), 1, 1,
            linewidth=1.2, edgecolor="black",
            facecolor=cmap(norm(val))
        )
    )

    ax.text(col + 0.5, -row + 0.62, elem,
            ha="center", va="center",
            fontsize=13, fontweight="bold")

    ax.text(col + 0.5, -row + 0.35, f"{val:.2f}",
            ha="center", va="center",
            fontsize=10)
# # Elements that need white text for visibility
# white_text_elements = {"Pd", "O"}
#
# for elem, (row, col) in positions.items():
#     val = values.get(elem, 0.0)
#
#     ax.add_patch(
#         patches.Rectangle(
#             (col, -row), 1, 1,
#             linewidth=1.2, edgecolor="black",
#             facecolor=cmap(norm(val))
#         )
#     )
#
#     text_color = "white" if elem in white_text_elements else "black"
#
#     ax.text(
#         col + 0.5, -row + 0.62, elem,
#         ha="center", va="center",
#         fontsize=13,
#         fontweight="bold",
#         color=text_color
#     )
#
#     ax.text(
#         col + 0.5, -row + 0.35, f"{val:.2f}",
#         ha="center", va="center",
#         fontsize=10,
#         color=text_color
#     )


ax.set_xlim(0, 18)
ax.set_ylim(-10, 1)
ax.axis("off")

sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
cbar.set_label("ΔF", fontsize=14, fontweight="bold")
cbar.ax.tick_params(labelsize=12)

plt.tight_layout()
plt.show()

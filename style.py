# style.py
# 2026 Joey Manani & Anchorfish Team
# Shared chart look for the EDA notebooks; one fixed colour per URL type
# Based on matplotlib's "Customizing Matplotlib with style sheets and rcParams" guide (setting mpl.rcParams once, up front):
# https://matplotlib.org/stable/users/explain/customizing.html

import matplotlib as mpl

# Blue / orange / violet / aqua
TYPE_COLOURS = {
    "Legitimate": "#2a78d6",  # blue
    "Phishing": "#eb6834",    # orange
    "Malware": "#4a3aa7",     # violet
    "Defacement": "#1baf7a",  # aqua
}
TYPE_ORDER = list(TYPE_COLOURS)

# raw Kaggle dataset label -> project label
# for future: supplementary datasets will use same labelling for consistency
KAGGLE_NAMES = {"benign": "Legitimate", "phishing": "Phishing", "malware": "Malware", "defacement": "Defacement"}

SURFACE      = "#fcfcfb"
INK          = "#0b0b0b"
INK_SOFT     = "#52514e"
MUTED        = "#898781"
GRID         = "#e1e0d9"
AXIS         = "#c3c2b7"

# correlations: blue (negative) -> grey (zero) -> red (positive) :D
DIVERGING = mpl.colors.LinearSegmentedColormap.from_list("blue_grey_red", ["#2a78d6", "#f0efec", "#e34948"])

DPI = 200 # good quality for exports and the report


def use() -> None:
    """Apply the shared look to every chart drawn after this call."""
    mpl.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "figure.figsize": (8, 4.5),
        "figure.dpi": 110,
        "font.family": "sans-serif",
        "font.sans-serif": ["Segoe UI", "Helvetica Neue", "Arial", "sans-serif"],
        "font.size": 10,
        "text.color": INK,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlepad": 12,
        "axes.labelsize": 10,
        "axes.labelcolor": INK_SOFT,
        "axes.edgecolor": AXIS,
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "axes.axisbelow": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelcolor": INK_SOFT,
        "ytick.labelcolor": INK_SOFT,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "legend.frameon": False,
        "legend.fontsize": 9,
        "patch.force_edgecolor": True,
        "patch.edgecolor": SURFACE,
        "patch.linewidth": 1.2,
        "lines.linewidth": 2,
        "lines.solid_capstyle": "round",
        "boxplot.medianprops.color": INK,
    })


def colours(types) -> list[str]:
    """Colour list for a sequence of type names, e.g. for pandas' color= argument."""
    return [TYPE_COLOURS[t] for t in types]


def save(fig, path) -> None:
    """Save a figure at print resolution with no clipped labels."""
    fig.savefig(path, dpi=DPI, bbox_inches="tight")

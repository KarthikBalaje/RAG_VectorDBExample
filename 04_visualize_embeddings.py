# ============================================================
#  SCRIPT 04 — Visualising Embeddings in 2D (FIXED VERSION)
# ============================================================

import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
except (AttributeError, RuntimeError, ValueError):
    pass

import chromadb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA

DB_PATH         = "./chroma_db"
COLLECTION_NAME = "rag_demo"

COLORS = {
    "Cars":  "#4C72B0",
    "Bikes": "#55A868",
}

# ── Load data safely ────────────────────────────────────────
db         = chromadb.PersistentClient(path=DB_PATH)
collection = db.get_or_create_collection(name=COLLECTION_NAME)

all_data = collection.get(include=["embeddings", "metadatas", "documents"])

ids = all_data.get("ids") or []

# --- embeddings (SAFE) ---
raw_embeddings = all_data.get("embeddings")
if raw_embeddings is None or len(raw_embeddings) == 0:
    print("Error: No embeddings found")
    sys.exit(1)
else:
    embeddings = np.array(raw_embeddings)

# --- metadata ---
metadatas = all_data.get("metadatas")
if metadatas is None:
    metadatas = []

# --- documents ---
documents = all_data.get("documents")
if documents is None:
    documents = []

if embeddings.size == 0 or len(metadatas) == 0:
    print("Error: No data found in collection")
    sys.exit(1)

print("=" * 60)
print("EMBEDDING VISUALISER")
print("=" * 60)

n_docs, n_dims = embeddings.shape
print(f"\nLoaded {n_docs} documents")
print(f"Embedding matrix shape: {embeddings.shape}")
print(f"  → {n_docs} documents × {n_dims} dimensions")

# ── PCA: reduce high-dim → 2D ───────────────────────────────
if n_docs < 2:
    print("Not enough data for PCA")
    sys.exit(1)

print(f"\nRunning PCA to compress {n_dims} dimensions → 2 ...")
pca    = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(embeddings)   # shape: (N, 2)

var_explained = pca.explained_variance_ratio_
print(
    f"Variance explained: "
    f"{var_explained[0]*100:.1f}% + {var_explained[1]*100:.1f}% = "
    f"{sum(var_explained)*100:.1f}%"
)

# ── Plot ───────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle("Document Embeddings Visualised in 2D (PCA)", fontsize=15, fontweight="bold")

categories = [str(m.get("category", "Unknown")) for m in metadatas]

# ── LEFT PLOT ──────────────────────────────────────────────
ax1 = axes[0]
ax1.set_title("Colour by Category")

for i, (x, y) in enumerate(coords):
    cat   = categories[i]
    color = COLORS.get(cat, "#999999")
    ax1.scatter(x, y, color=color, s=120, edgecolors="white")

# Labels
# Labels (SAFE)
for i, (x, y) in enumerate(coords):
    meta = metadatas[i] if i < len(metadatas) else {}

    if not isinstance(meta, dict):
        meta = {}

    title = meta.get("title", "Unknown")

    # Ensure title is string
    if not isinstance(title, str):
        title = str(title)

    title = title if len(title) < 20 else title[:18] + "…"

    ax1.annotate(
        title,
        (float(x), float(y)),   # ensure numeric
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=7
    )

# Legend
patches = [mpatches.Patch(color=c, label=cat) for cat, c in COLORS.items()]
ax1.legend(handles=patches)

ax1.set_xlabel(f"PC1 ({var_explained[0]*100:.1f}%)")
ax1.set_ylabel(f"PC2 ({var_explained[1]*100:.1f}%)")
ax1.grid(True)

# ── RIGHT PLOT ─────────────────────────────────────────────
ax2 = axes[1]
ax2.set_title("Cluster View")

for i, (x, y) in enumerate(coords):
    cat   = categories[i]
    color = COLORS.get(cat, "#999999")
    ax2.scatter(x, y, color=color, s=200, alpha=0.7, edgecolors="white")
    ax2.text(x, y, cat[0], ha="center", va="center", color="white", fontweight="bold")

ax2.legend(handles=patches)
ax2.set_xlabel(f"PC1 ({var_explained[0]*100:.1f}%)")
ax2.set_ylabel(f"PC2 ({var_explained[1]*100:.1f}%)")
ax2.grid(True)

# ── Save & Show ────────────────────────────────────────────
plt.tight_layout()
plt.savefig("embedding_clusters.png", dpi=150)
print("\nPlot saved → embedding_clusters.png")
plt.show()

# ── Coordinates Table ──────────────────────────────────────
print("\n── 2D coordinates after PCA ─────────────────────────────")

print(f"\n  {'ID':15s}  {'Category':12s}  {'PC1':>10}  {'PC2':>10}")
print("  " + "-" * 52)

for i, doc_id in enumerate(ids):
    x, y = coords[i]
    cat  = categories[i] if i < len(categories) else "Unknown"
    print(f"  {doc_id:15s}  {cat:12s}  {x:>10.4f}  {y:>10.4f}")

print("\nKey insight:")
print("  Similar documents cluster together in vector space.")
print("  Vector DBs work by finding nearest neighbours.")

print("\n✓ Script 04 complete. Run 05_query_and_retrieve.py next.")
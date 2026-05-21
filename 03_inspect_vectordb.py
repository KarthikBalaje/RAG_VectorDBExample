# ============================================================
#  SCRIPT 03 — Inspecting the Vector Database (FIXED VERSION)
# ============================================================

import os
import sys
import math

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
except (AttributeError, RuntimeError, ValueError):
    pass

import chromadb

DB_PATH         = "./chroma_db"
COLLECTION_NAME = "rag_demo"


# ── Connect ─────────────────────────────────────────────────
db         = chromadb.PersistentClient(path=DB_PATH)
collection = db.get_or_create_collection(name=COLLECTION_NAME)

total = collection.count()
print("=" * 60)
print(f"VECTOR DATABASE INSPECTOR  ({total} documents stored)")
print("=" * 60)


# ── Helper (SAFE) ───────────────────────────────────────────
def cosine_similarity(a, b):
    dot   = sum(float(x) * float(y) for x, y in zip(a, b))
    mag_a = math.sqrt(sum(float(x) ** 2 for x in a))
    mag_b = math.sqrt(sum(float(y) ** 2 for y in b))

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot / (mag_a * mag_b)


# ── Fetch all data ──────────────────────────────────────────
print("\n── All stored document IDs ──────────────────────────────")
all_data = collection.get(include=["metadatas", "embeddings", "documents"])

ids = all_data.get("ids")
if ids is None:
    ids = []

metadatas = all_data.get("metadatas")
if metadatas is None:
    metadatas = []

documents = all_data.get("documents")
if documents is None:
    documents = []

embeddings = all_data.get("embeddings")
if embeddings is None:
    embeddings = []


# ── SECTION 1: All stored IDs ───────────────────────────────
if ids and metadatas:
    for i, (doc_id, meta) in enumerate(zip(ids, metadatas), 1):
        print(
            f"  {i:02d}.  {doc_id:15s}  "
            f"[{meta.get('category','N/A'):10s}]  "
            f"{meta.get('title','N/A')}"
        )
else:
    print("  No data found in collection")


# ── SECTION 2: Metadata table ───────────────────────────────
print("\n── Metadata stored with each document ───────────────────")

header = f"  {'ID':15s}  {'Title':30s}  {'Category':12s}  {'Source':25s}  {'Year'}"
print(header)
print("  " + "-" * (len(header) - 2))

if ids and metadatas:
    for doc_id, meta in zip(ids, metadatas):
        print(
            f"  {doc_id:15s}  "
            f"{meta.get('title','N/A'):30s}  "
            f"{meta.get('category','N/A'):12s}  "
            f"{meta.get('source','N/A'):25s}  "
            f"{meta.get('year','N/A')}"
        )


# ── SECTION 3: Show a full vector ───────────────────────────
print("\n── Full vector for 'car_001' ───────────────────────────")

if "car_001" in ids:
    idx = ids.index("car_001")

    vec = embeddings[idx] if embeddings is not None and len(embeddings) > idx else None
    text = documents[idx] if documents is not None and len(documents) > idx else None
else:
    vec, text = None, None

if vec is not None and text is not None:
    print(f"\n  Document text:\n  '{text[:100]}...'")

    dims = len(vec)
    print(f"\n  Vector length: {dims} dimensions")
    print(f"\n  Values (showing first 20 out of {dims}):")

    ROW = 5
    for i in range(0, min(20, len(vec)), ROW):
        chunk = vec[i:i+ROW]
        formatted = "  ".join(f"{float(v): .5f}" for v in chunk)
        print(f"  [{i:4d}-{i+ROW-1:4d}]  {formatted}")

    print(f"  ... (remaining {dims - 20} values not shown)")
else:
    print("  Unable to retrieve vector data")


# ── SECTION 4: Two vectors side-by-side ─────────────────────
print("\n── Two vectors side-by-side (first 10 dims) ─────────────")

vec_a, vec_b = None, None

if "car_001" in ids and "bike_001" in ids:
    idx_a = ids.index("car_001")
    idx_b = ids.index("bike_001")

    if embeddings is not None and len(embeddings) > max(idx_a, idx_b):
        vec_a = embeddings[idx_a]
        vec_b = embeddings[idx_b]

if vec_a is not None and vec_b is not None:
    print(f"\n  {'Dim':>5}  {'car_001':>12}  {'bike_001':>12}  {'Difference':>12}")
    print(f"  {'---':>5}  {'----------':>12}  {'----------':>12}  {'----------':>12}")

    for i in range(10):
        diff = float(vec_a[i]) - float(vec_b[i])
        print(f"  {i:>5}  {float(vec_a[i]):>12.6f}  {float(vec_b[i]):>12.6f}  {diff:>+12.6f}")

    sim = cosine_similarity(vec_a, vec_b)
    print(f"\n  Cosine similarity between car_001 and bike_001: {sim:.4f}")
    print("  (If this is close to 1.0 → similar. Close to 0 → different.)")
else:
    print("\n  Unable to retrieve vectors for comparison")


# ── SECTION 5: Mini similarity matrix ───────────────────────
print("\n── Similarity matrix (one doc per category) ─────────────")

sample_ids    = ["car_001", "car_011", "bike_001", "bike_011"]
sample_labels = ["Car-1", "Car-2", "Bike-1", "Bike-2"]

sample_vecs = []
labels = []

for sid, lbl in zip(sample_ids, sample_labels):
    if sid in ids and embeddings is not None:
        idx = ids.index(sid)

        if idx < len(embeddings):
            sample_vecs.append(embeddings[idx])
            labels.append(lbl)

# Header
header_row = f"  {'':8s}" + "".join(f"  {l:8s}" for l in labels)
print(f"\n{header_row}")

# Matrix
for label_i, vec_i in zip(labels, sample_vecs):
    row = f"  {label_i:8s}"
    for vec_j in sample_vecs:
        sim = cosine_similarity(vec_i, vec_j)
        row += f"  {sim:8.4f}"
    print(row)

print("\n  Diagonal = 1.0 (self similarity)")
print("  Same-topic docs → HIGH similarity")
print("  Cross-topic docs → LOWER similarity")

print("\n✓ Script 03 complete. Run 04_visualize_embeddings.py next.")
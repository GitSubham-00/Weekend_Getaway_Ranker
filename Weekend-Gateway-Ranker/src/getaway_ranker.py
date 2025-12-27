import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/Top_Indian_Places_to_Visit.csv")
df.columns = df.columns.str.strip()

# -----------------------------
# Zone adjacency mapping
# -----------------------------
ZONE_ADJACENCY = {
    "Eastern": ["Eastern", "Northern"],
    "Northern": ["Northern", "Eastern", "Western"],
    "Western": ["Western", "Northern", "Southern"],
    "Southern": ["Southern", "Western"]
}

# -----------------------------
# Distance score logic
# -----------------------------
def compute_distance_score(dest_city, dest_state, dest_zone,
                           src_city, src_state, src_zone):
    if dest_city == src_city:
        return 1.0          # Same city (local weekend)
    elif dest_state == src_state:
        return 0.9          # Same state
    elif dest_zone == src_zone:
        return 0.75         # Same zone
    elif dest_zone in ZONE_ADJACENCY.get(src_zone, []):
        return 0.6          # Adjacent zone
    else:
        return 0.35         # Far

# -----------------------------
# Ranking function
# -----------------------------
def rank_weekend_destinations(source_city, top_n=5):

    if source_city not in df["City"].values:
        raise ValueError("Source city not found in dataset")

    source_state = df.loc[df["City"] == source_city, "State"].iloc[0]
    source_zone = df.loc[df["City"] == source_city, "Zone"].iloc[0]

    candidates = df.copy()

    # Weekend-friendly filters
    candidates = candidates[
        (candidates["time needed to visit in hrs"] <= 5) &
        (candidates["Google review rating"] >= 4.0)
    ]

    # Distance score
    candidates["distance_score"] = candidates.apply(
        lambda x: compute_distance_score(
            x["City"], x["State"], x["Zone"],
            source_city, source_state, source_zone
        ),
        axis=1
    )

    # Normalize rating
    candidates["rating_norm"] = (
        candidates["Google review rating"] /
        candidates["Google review rating"].max()
    )

    # Normalize popularity
    candidates["popularity_norm"] = (
        candidates["Number of google review in lakhs"] /
        candidates["Number of google review in lakhs"].max()
    )

    # Final weighted score
    candidates["final_score"] = (
        0.45 * candidates["distance_score"] +
        0.35 * candidates["rating_norm"] +
        0.20 * candidates["popularity_norm"]
    )

    result = (
        candidates.sort_values("final_score", ascending=False)
        .head(top_n)[[
            "Name",
            "City",
            "State",
            "Zone",
            "Google review rating",
            "Number of google review in lakhs",
            "Best Time to visit",
            "final_score"
        ]]
    )

    return result.reset_index(drop=True)

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":

    user_city = input(
        "\nEnter a source city (or press Enter to run sample cities): "
    ).strip()

    if user_city:
        print(f"\nTop Weekend Destinations from {user_city}")
        print(rank_weekend_destinations(user_city))
    else:
        for city in ["Kolkata", "Delhi", "Mumbai"]:
            print(f"\nTop Weekend Destinations from {city}")
            print(rank_weekend_destinations(city))

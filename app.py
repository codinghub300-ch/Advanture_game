import streamlit as st
import random

st.set_page_config(
    page_title="Multi-World Adventure Game",
    page_icon="⚔️"
)

# ==========================
# Game Data
# ==========================

locations = {
    "Haunted Forest": {
        "enemies": ["Ghost", "Werewolf", "Witch"],
        "weapons": ["Silver Sword", "Crossbow", "Magic Light"],
        "treasures": ["Enchanted Ring", "Glowing Gem", "Ancient Spellbook"]
    },
    "Abandoned Castle": {
        "enemies": ["Skeleton Knight", "Dark Mage", "Giant Rat"],
        "weapons": ["Flaming Axe", "Holy Spear", "Bow and Arrow"],
        "treasures": ["Gold Crown", "Royal Scepter", "Hidden Gold Chest"]
    },
    "Mysterious Cave": {
        "enemies": ["Bat Swarm", "Stone Golem", "Lava Serpent"],
        "weapons": ["Torch", "Pickaxe", "Ice Spell"],
        "treasures": ["Crystal Shards", "Fossil Relic", "Diamond Cluster"]
    },
    "Enchanted Valley": {
        "enemies": ["Evil Fairy", "Forest Spirit", "Wild Unicorn"],
        "weapons": ["Net Trap", "Singing Flute", "Spirit Orb"],
        "treasures": ["Blessed Flower", "Star Dust", "Rainbow Crystal"]
    }
}

difficulty_ranges = {
    "Easy": (1, 6),
    "Medium": (4, 8),
    "Hard": (6, 10)
}

# ==========================
# Session State
# ==========================

if "score" not in st.session_state:
    st.session_state.score = 0

if "stage" not in st.session_state:
    st.session_state.stage = "explore"

# ==========================
# Header
# ==========================

st.title("⚔️ Multi-World Adventure Game")

st.markdown("""
🌟 Welcome to the Multi-World Adventure Game! 🌟

Explore mysterious places, fight enemies, and collect treasures to gain points.
""")

st.success(f"🎯 Current Score: {st.session_state.score}")

# ==========================
# Difficulty
# ==========================

difficulty = st.selectbox(
    "🎮 Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

# ==========================
# Explore Stage
# ==========================

if st.session_state.stage == "explore":

    location = st.selectbox(
        "🧭 Choose a Location",
        list(locations.keys())
    )

    if st.button("🚀 Explore"):

        st.session_state.location = location
        st.session_state.enemy = random.choice(
            locations[location]["enemies"]
        )

        st.session_state.weapon = random.choice(
            locations[location]["weapons"]
        )

        st.session_state.treasure = random.choice(
            locations[location]["treasures"]
        )

        st.session_state.stage = "fight"

        st.rerun()

# ==========================
# Fight Stage
# ==========================

elif st.session_state.stage == "fight":

    st.subheader(
        f"🧭 You are heading into the {st.session_state.location}"
    )

    st.warning(
        f"👾 A wild {st.session_state.enemy} appears!"
    )

    st.info(
        f"🗡 You grab {st.session_state.weapon} to defend yourself."
    )

    action = st.radio(
        "What do you want to do?",
        ["Fight", "Run Away"]
    )

    if st.button("Continue"):

        if action == "Fight":

            player_strength = random.randint(1, 10)

            enemy_strength = random.randint(
                *difficulty_ranges[difficulty]
            )

            st.session_state.player_strength = player_strength
            st.session_state.enemy_strength = enemy_strength

            if player_strength >= enemy_strength:
                st.session_state.result = "win"
                st.session_state.score += 10
            else:
                st.session_state.result = "lose"

        else:
            st.session_state.result = "run"

        st.session_state.stage = "result"

        st.rerun()

# ==========================
# Result Stage
# ==========================

elif st.session_state.stage == "result":

    if st.session_state.result == "win":

        st.write(
            f"💪 Your Strength: {st.session_state.player_strength}"
        )

        st.write(
            f"👾 Enemy Strength: {st.session_state.enemy_strength}"
        )

        st.success(
            f"🎉 Victory! You defeated the {st.session_state.enemy}"
        )

        st.success(
            f"🏆 You found {st.session_state.treasure}"
        )

    elif st.session_state.result == "lose":

        st.write(
            f"💪 Your Strength: {st.session_state.player_strength}"
        )

        st.write(
            f"👾 Enemy Strength: {st.session_state.enemy_strength}"
        )

        st.error(
            f"💀 You were defeated by the {st.session_state.enemy}"
        )

    else:

        st.warning(
            f"🏃 You ran away from the {st.session_state.enemy}"
        )

    st.success(
        f"🎯 Total Score: {st.session_state.score}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌍 Explore Another Place"):
            st.session_state.stage = "explore"
            st.rerun()

    with col2:
        if st.button("🔄 Restart Game"):
            st.session_state.score = 0
            st.session_state.stage = "explore"
            st.rerun()
            

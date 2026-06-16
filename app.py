import streamlit as st
import random

st.set_page_config(
    page_title="Adventure Game",
    page_icon="⚔️",
    layout="centered"
)

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

st.title("⚔️ Multi-World Adventure Game")

if "score" not in st.session_state:
    st.session_state.score = 0

difficulty = st.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

difficulty_ranges = {
    "Easy": (1, 6),
    "Medium": (4, 8),
    "Hard": (6, 10)
}

selected_location = st.selectbox(
    "Choose a Location",
    list(locations.keys())
)

if st.button("🚀 Explore"):
    
    enemy = random.choice(locations[selected_location]["enemies"])
    weapon = random.choice(locations[selected_location]["weapons"])
    treasure = random.choice(locations[selected_location]["treasures"])

    st.session_state.enemy = enemy
    st.session_state.weapon = weapon
    st.session_state.treasure = treasure

if "enemy" in st.session_state:

    st.warning(
        f"A wild {st.session_state.enemy} appeared!"
    )

    st.info(
        f"You picked up {st.session_state.weapon}"
    )

    action = st.radio(
        "What will you do?",
        ["Fight", "Run Away"]
    )

    if st.button("⚔️ Continue"):

        if action == "Fight":

            player_strength = random.randint(1, 10)

            enemy_strength = random.randint(
                *difficulty_ranges[difficulty]
            )

            st.write(
                f"Your Strength: {player_strength}"
            )

            st.write(
                f"Enemy Strength: {enemy_strength}"
            )

            if player_strength >= enemy_strength:

                st.success(
                    f"🎉 Victory! You defeated the {st.session_state.enemy}"
                )

                st.success(
                    f"🏆 You found {st.session_state.treasure}"
                )

                st.session_state.score += 10

            else:

                st.error(
                    f"💀 Defeat! The {st.session_state.enemy} defeated you."
                )

        else:

            st.warning(
                "🏃 You escaped safely."
            )

st.markdown("---")

st.subheader(
    f"🎯 Current Score: {st.session_state.score}"
)

if st.button("🔄 Reset Game"):
    st.session_state.score = 0
    st.rerun()
  

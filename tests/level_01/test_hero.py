"""Level 01 · First Blood. Your mission is in README.md in this folder.

Write your tests in this file (you may add more test_*.py files too).

    Run your tests:      pytest tests/level_01 -v
    Ask the grader:      python -m grader check 1
    Done? Commit it:     git add tests/level_01  then  git commit
"""

from dungeon.hero import Hero

# --- New Hero hp ---
def test_new_hero_hp_has_full_health():
    hero = Hero("Ada")
    assert hero.hp == 100


# --- take_damage ---
def test_take_damage_never_goes_below_zero():
    hero = Hero("Ada", hp=15)
    hero.take_damage(16)
    assert hero.hp == 0

def test_take_damage_changes_hero_hp():
    hero = Hero("Ada", hp=17)
    hero.take_damage(16)
    assert hero.hp == 1


# --- heal ---
def test_heal_raises_hp():
    hero = Hero("Ada", hp=10)
    hero.heal(89)
    assert hero.hp == 99

def test_heal_never_goes_above_max_hp():
    hero = Hero("Ada")
    hero.heal(100)
    assert hero.hp == 100


# --- is_alive ---
def test_hero_is_alive_with_1_hp():
    hero = Hero("Ada")
    hero.take_damage(99)
    assert hero.is_alive

def test_hero_is_not_alive_with_0_hp():
    hero = Hero("Ada")
    hero.take_damage(100)
    assert not hero.is_alive 


# --- gain_xp ---
def test_100_xp_gives_one_level():
    hero = Hero("Ada")
    hero.gain_xp(100)
    assert hero.level == 2

def test_250_xp_changes_levels_by_two():
    hero = Hero("Ada")
    hero.gain_xp(250)
    assert hero.level == 3

def test_250_xp_returns_number_two():
    hero = Hero("Ada")
    levels = hero.gain_xp(250)
    assert levels == 2

def test_250_xp_gives_50_xp_left():
    hero = Hero("Ada")
    hero.gain_xp(250)
    assert hero.xp == 50
import pytest

from dungeon.hero import Hero
from dungeon.inventory import Inventory, Item
from dungeon.shop import Listing, Shop


# --- Hero ---
@pytest.fixture
def hero():
    """A brand-new hero called Ada with no gold."""
    return Hero("Ada")


@pytest.fixture
def rich_hero(hero):
    """The `hero` fixture with 100 gold: enough for a potion, not for a bazooka."""
    hero.gold = 100
    return hero


# --- Backpack ---
@pytest.fixture
def backpack():
    """An empty backpack with the default weight limit (20 kg)."""
    return Inventory()


@pytest.fixture
def full_backpack(backpack, potion):
    """The `backpack` fixture filled to its 20 kg limit with 40 potions."""
    backpack.add(potion, 40)
    return backpack


# --- Items ---
@pytest.fixture
def potion():
    """A light, cheap item: 0.5 kg, worth 5 gold."""
    return Item("Potion", 0.5, 5)


@pytest.fixture
def bazooka():
    """A heavy, valuable item: 5.3 kg, worth 20 gold."""
    return Item("Bazooka", 5.3, 20)


# --- Shop ---
@pytest.fixture
def shop(potion, bazooka):
    """A shop selling potions (10 gold, 2 in stock) and bazookas (125 gold, 7 in stock)."""
    potion_listing = Listing(potion, 10, 2)
    bazooka_listing = Listing(bazooka, 125, 7)
    return Shop([potion_listing, bazooka_listing])

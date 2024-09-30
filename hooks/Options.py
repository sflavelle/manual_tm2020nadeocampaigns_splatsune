# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionSet

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from .Data import supported_campaigns



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class CampaignsToWin(Range):
    """The number of campaigns on which you need to finish Track #25."""
    display_name = "Campaigns To Complete"
    range_start = 1
    range_end = len(supported_campaigns())
    default = 1

class CampaignSelection(OptionSet):
    """The campaigns you either have available, or would like to play.
    Note that the more campaigns you select, the longer your seed will be."""
    display_name = "Select Available Campaigns"
    valid_keys = [key for key in supported_campaigns()]

class ExcludeImpossibleMedals(DefaultOnToggle):
    """Exclude medals that have been made extremely difficult
    or impossible due to physics changes.
    The only reason to turn this off is if you are a pro
    TrackMania player."""
    display_name = "Exclude Impossible Medals"
    # Currently: Summer 2020 #10, 

class IncludeAuthorMedals(Toggle):
    """Allow author medals to be included as locations.
    Author Medals are the time recorded by the map author,
    and are often difficult to attain for a newer player."""
    display_name = "Include Author Medal Locations"

class IncludeTrophies(Toggle):
    """Allow trophies to be included as locations.
    Trophies are given based on the worst medal attained in each set of 5 tracks.
    For example, a set with 4 golds and 1 bronze medal will give you a Bronze Trophy."""
    display_name = "Include Trophy Locations"


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:

    options["campaigns"] = CampaignSelection
    options["goal_campaigns"] = CampaignsToWin

    options["exclude_impossible_medals"] = ExcludeImpossibleMedals
    options["author_medals"] = IncludeAuthorMedals
    options["trophies"] = IncludeTrophies

    options["shuffle_vehicles"].display_name = "Shuffle Vehicles into Pool"
    options["shuffle_vehicles"].__doc__ = """Allow vehicles to be shuffled into the item pool.
    The default vehicle is the Stadium Car,
    but levels may force you to start as a vehicle with different properties,
    or switch you to a different vehicle mid-track.
    You will start with a random vehicle unlocked, which will affect what levels you can access."""

    return options
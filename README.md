An implementation of the [Archipelago Manual World](https://github.com/ManualForArchipelago/Manual) for Trackmania (2020). This world in particular is for playing through official campaigns.

**This world may not generate, mostly with smaller games, and has minimal items until these issues are resolved.**

## How to install
- Download the latest `.apworld` from [Releases](https://github.com/sflavelle/manual_tm2020nadeocampaigns_splatsune/releases/latest), and open it in Archipelago 0.5.0 or later to install it to your client.

## How to Play

In your Archipelago Launcher, use the **Manual Client** to log in and play using this world.

**You will need a Club Subscription to Trackmania to be able to play this world.**

### Rule Set
The basics of how this world works is vaguely modelled on the gated progression of standard play, with an extra gate on the Green tracks and without medals to collect (for now). Here's how it works:

- Receiving a Progressive Unlock for a campaign gives you access to the White tracks in that campaign (the first five tracks).
- Receiving more Progressive Unlocks gives you access to the next tiers: In order, they are White, Green, Blue, Red, and Black.
- Your goal on each campaign is to finish Map #25 with a Gold Medal. Once you collect the amount of completion tokens specified in your YAML options file, that is Victory!

## Locations

There are currently **18** campaigns available, from **Summer 2020** to **Fall 2024**.

- 4 medals per map (Bronze, Silver, Gold, Author) (100 locations per campaign)
    - *Author medals may be disabled via YAML*
- 4 trophies per tier (all Bronze, all Silver, all Gold, all Author) (20 locations per campaign)
    - Trophies are based on your *worst* medal obtained in each tier, ie. 4 Gold and 1 Silver earns a Silver Trophy
    - *Trophies may be disabled per YAML*
from discord.ext import commands
import requests, random
discord_token = 'meow'

not_a_self_bot = commands.Bot(command_prefix='::!:!:Ds[apodaso[djkasd]]')
not_a_self_bot.remove_command('help')

@not_a_self_bot.event
async def on_connect():
    panes = ['My Account', 'Authorized Apps', 'Sessions', 'Connections', 'Friend Requests', 'Discord Nitro', 'Nitro Server Boost', 'Subscriptions', 'Library Inventory', 'Billing', 'Appearance', 'Accessibility', 'Voice & Video', 'Text & Images', 'Notifications', 'Keybinds', 'Language', 'Streamer Mode', 'Advanced', 'Activity Privacy', 'Game Activity', 'Hypesquad Online']

    #                   vv - idk what the fuck this is but i pasted it from my alt incase 
    #                   vv   it matters or something lol [plz don doxz meee :)!!!!]
    payload = {'token':'MTA1MTE4NjMxMjkwMTgyNDU1Mw.WN7zwN4Va94_BAKXA73E4inqclI', 'events':[{'type':'settings_pane_viewed', 'properties': {'destination_pane': random.choice(panes)}}]}

    request = requests.post('https://discord.com/api/v9/science', json=payload, headers={'authorization': discord_token, 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTYyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='})

    print('ready mr sir')

not_a_self_bot.run(discord_token)
import art
from inquirer import Text, List, prompt
from Bots.Zefoy import ZefoyAutomator


print(art.LOGO_ART)



questions = [
    Text("post_url", message=art.input_style + "Enter Tiktok URL here"),
    List("type", message=art.input_style + "What stat do you want to bot (Use arrows to choose)?",
         choices=["followers", "hearts", "comment_hearts", "views", "shares", "favorites", "live_stream"]
         )
]

answers = prompt(questions)

botter = ZefoyAutomator(answers["post_url"], type=answers["type"])
botter.launch()
botter.send()
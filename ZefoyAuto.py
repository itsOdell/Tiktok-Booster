import art
from inquirer import Text, List, prompt
from Bots import Zefoy


print(art.LOGO_ART)

questions = [
    Text("post_url", message="Enter Tiktok URL here"),
    List("type", message="What stat do you want to bot (Use arrows to choose)?",
         choices=["followers", "hearts", "comment_hearts", "views", "shares", "favorites", "live_stream"]
         )
]

answers = prompt(questions)
botter = Zefoy(answers["post_url"], answers["type"])
botter.launch()
botter.send()
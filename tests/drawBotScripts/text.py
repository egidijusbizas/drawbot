import drawBot
drawBot.size(200, 200)
drawBot.text("hello world", (10, 10))
drawBot.fill(1, 0, 0)
drawBot.text("foo bar", (10, 30))
drawBot.fill(1, 0, 1)
drawBot.stroke(0, 1, 0)
drawBot.strokeWidth(2)
drawBot.font("Times", 50)
drawBot.text("foo bar", (10, 50))
drawBot.fill(None)
drawBot.stroke(0, 1, 0)
drawBot.strokeWidth(1)
drawBot.line((0, 50), (drawBot.width(), 50))
drawBot.stroke(None)
drawBot.fill(0, 1, 1)
drawBot.fontSize(20)
drawBot.text("foo bar", (drawBot.width()*.5, 100), align="right")
drawBot.text("foo bar", (drawBot.width()*.5, 120), align="center")
drawBot.text("foo bar", (drawBot.width()*.5, 140), align="left")
mineflayer = require('mineflayer')

options = {
    "username":"traumaturgist",
    "host":"Dragon_tech.aternos.me",
    "port":24622,
    "version":'1.20.1'
}

bot = mineflayer.createBot(options)

const attack = () => {
    bot.attack(bot.entityAtCursor())
}

const lookat = (whisperer) =>{
    bot.chat(whisperer)
    player = bot.players[whisperer]
    if (player){
        bot.chat(player.position.toString())
    }
    //bot.lookAt()
}

const ToggleSprint = () => {
    bot.setControlState('sprint',!bot.getControlState('sprint'))
}

const skull = () =>{
    bot.chat('skull')
}

bot.once('spawn',skull)
bot.on('whisper',lookat)
bot.on('chat',attack)